// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "TableLog.h"

#include <bitset>
#include <cstdint>
#include <map>
#include <optional>
#include <stdexcept>
#include <utility>

#include "Column.h"
#include "IntColumn.h"
#include "LogCache.h"
#include "LogEntry.h"
#include "Logfile.h"
#include "MonitoringCore.h"
#include "Query.h"
#include "Row.h"
#include "StringColumn.h"
#include "TableCommands.h"
#include "TableContacts.h"
#include "TableHosts.h"
#include "TableServices.h"
#include "TimeColumn.h"
#include "auth.h"

#ifdef CMC
#include "cmc.h"
class Contact;
class Host;
class Service;
#else
#include "nagios.h"
#endif

namespace {

class LogRow {
public:
    // TODO(sp): Remove ugly casts.
    LogRow(const LogEntry &entry_, MonitoringCore *mc)
        : entry{&entry_}
        , hst{reinterpret_cast<host *>(mc->find_host(entry_.host_name()))}
        , svc{reinterpret_cast<service *>(mc->find_service(
              entry_.host_name(), entry_.service_description()))}
        , ctc{reinterpret_cast<const contact *>(
              mc->find_contact(entry_.contact_name()))}
        , command{mc->find_command(entry_.command_name())} {}

    const LogEntry *entry;
    host *hst;
    service *svc;
    const contact *ctc;
    Command command;
};

}  // namespace

TableLog::TableLog(MonitoringCore *mc, LogCache *log_cache)
    : Table(mc), _log_cache(log_cache) {
    ColumnOffsets offsets{};
    auto offsets_entry{
        offsets.add([](Row r) { return r.rawData<LogRow>()->entry; })};
    addColumn(std::make_unique<TimeColumn<LogEntry>>(
        "time", "Time of the log event (UNIX timestamp)", offsets_entry,
        [](const LogEntry &r) { return r.time(); }));
    addColumn(std::make_unique<IntColumn<LogEntry>>(
        "lineno", "The number of the line in the log file", offsets_entry,
        [](const LogEntry &r) { return r.lineno(); }));
    addColumn(std::make_unique<IntColumn<LogEntry>>(
        "class",
        "The class of the message as integer (0:info, 1:state, 2:program, 3:notification, 4:passive, 5:command)",
        offsets_entry,
        [](const LogEntry &r) { return static_cast<int32_t>(r.log_class()); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "message", "The complete message line including the timestamp",
        offsets_entry, [](const LogEntry &r) { return r.message(); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "type",
        "The type of the message (text before the colon), the message itself for info messages",
        offsets_entry, [](const LogEntry &r) { return r.type(); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "options", "The part of the message after the ':'", offsets_entry,
        [](const LogEntry &r) { return r.options(); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "comment", "A comment field used in various message types",
        offsets_entry, [](const LogEntry &r) { return r.comment(); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "plugin_output",
        "The output of the check, if any is associated with the message",
        offsets_entry, [](const LogEntry &r) { return r.plugin_output(); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "long_plugin_output",
        "The complete output of the check, if any is associated with the message",
        offsets_entry,
        [](const LogEntry &r) { return r.long_plugin_output(); }));
    addColumn(std::make_unique<IntColumn<LogEntry>>(
        "state", "The state of the host or service in question", offsets_entry,
        [](const LogEntry &r) { return r.state(); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "state_type", "The type of the state (varies on different log classes)",
        offsets_entry, [](const LogEntry &r) { return r.state_type(); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "state_info", "Additional information about the state", offsets_entry,
        [](const LogEntry &r) { return r.state_info(); }));
    addColumn(std::make_unique<IntColumn<LogEntry>>(
        "attempt", "The number of the check attempt", offsets_entry,
        [](const LogEntry &r) { return r.attempt(); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "service_description",
        "The description of the service log entry is about (might be empty)",
        offsets_entry,
        [](const LogEntry &r) { return r.service_description(); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "host_name",
        "The name of the host the log entry is about (might be empty)",
        offsets_entry, [](const LogEntry &r) { return r.host_name(); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "contact_name",
        "The name of the contact the log entry is about (might be empty)",
        offsets_entry, [](const LogEntry &r) { return r.contact_name(); }));
    addColumn(std::make_unique<StringColumn<LogEntry>>(
        "command_name",
        "The name of the command of the log entry (e.g. for notifications)",
        offsets_entry, [](const LogEntry &r) { return r.command_name(); }));

    // join host and service tables
    TableHosts::addColumns(this, "current_host_", offsets.add([](Row r) {
        return r.rawData<LogRow>()->hst;
    }));
    TableServices::addColumns(this, "current_service_", offsets.add([](Row r) {
        return r.rawData<LogRow>()->svc;
    }),
                              false /* no hosts table */);
    TableContacts::addColumns(this, "current_contact_", offsets.add([](Row r) {
        return r.rawData<LogRow>()->ctc;
    }));
    TableCommands::addColumns(this, "current_command_", offsets.add([](Row r) {
        return &r.rawData<LogRow>()->command;
    }));
}

std::string TableLog::name() const { return "log"; }

std::string TableLog::namePrefix() const { return "log_"; }

void TableLog::answerQuery(Query *query) {
    _log_cache->apply([this, query](const LogFiles &log_files) {
        answerQueryInternal(query, log_files);
    });
}

void TableLog::answerQueryInternal(Query *query, const LogFiles &log_files) {
    if (log_files.begin() == log_files.end()) {
        return;
    }

    // Optimize time interval for the query. In log querys there should always
    // be a time range in form of one or two filter expressions over time. We
    // use that to limit the number of logfiles we need to scan and to find the
    // optimal entry point into the logfile
    auto since = std::chrono::system_clock::from_time_t(
        query->greatestLowerBoundFor("time").value_or(0));
    auto now =
        std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
    auto until = std::chrono::system_clock::from_time_t(
        query->leastUpperBoundFor("time").value_or(now) + 1);

    // The second optimization is for log message types. We want to load only
    // those log type that are queried.
    auto classmask = query->valueSetLeastUpperBoundFor("class")
                         .value_or(~std::bitset<32>())
                         .to_ulong();
    if (classmask == 0) {
        return;
    }
    auto max_lines_per_logfile = core()->maxLinesPerLogFile();
    auto processEntry = [core = core(), query](const LogEntry &entry) {
        LogRow r{entry, core};
        return query->processDataset(Row{&r});
    };

    auto it = log_files.end();  // it now points beyond last log file
    --it;                       // switch to last logfile (we have at least one)

    // Now find newest log where 'until' is contained. The problem
    // here: For each logfile we only know the time of the *first* entry,
    // not that of the last.
    while (it != log_files.begin() && it->second->since() > until) {
        // while logfiles are too new go back in history
        --it;
    }
    if (it->second->since() > until) {
        return;  // all logfiles are too new
    }

    while (true) {
        const auto *entries =
            it->second->getEntriesFor(max_lines_per_logfile, classmask);
        if (!answerQueryReverse(processEntry, entries, since, until)) {
            break;  // end of time range found
        }
        if (it == log_files.begin()) {
            break;  // this was the oldest one
        }
        --it;
    }
}

// static
bool TableLog::answerQueryReverse(
    const std::function<bool(const LogEntry &)> &processEntry,
    const Logfile::map_type *entries,
    std::chrono::system_clock::time_point since,
    std::chrono::system_clock::time_point until) {
    auto it = entries->upper_bound(Logfile::makeKey(until, 999999999));
    while (it != entries->begin()) {
        --it;
        const auto &entry = *it->second;
        if (entry.time() < since) {
            return false;  // time limit exceeded
        }
        if (!processEntry(entry)) {
            return false;
        }
    }
    return true;
}

namespace {
bool rowWithoutHost(const LogRow *lr) {
    auto clazz = lr->entry->log_class();
    return clazz == LogEntry::Class::info ||
           clazz == LogEntry::Class::program ||
           clazz == LogEntry::Class::ext_command;
}

}  // namespace

bool TableLog::isAuthorized(Row row, const contact *ctc) const {
    const auto *lr = rowData<LogRow>(row);
    // If we have an AuthUser, suppress entries for messages with hosts that do
    // not exist anymore.
    return lr->hst == nullptr  //
               ? ctc == no_auth_user() || rowWithoutHost(lr)
               : lr->svc == nullptr
                     ? is_authorized_for_hst(ctc, lr->hst)
                     : is_authorized_for_svc(core()->serviceAuthorization(),
                                             ctc, lr->svc);
}

std::shared_ptr<Column> TableLog::column(std::string colname) const {
    try {
        // First try to find column in the usual way
        return Table::column(colname);
    } catch (const std::runtime_error &e) {
        // Now try with prefix "current_", since our joined tables have this
        // prefix in order to make clear that we access current and not historic
        // data and in order to prevent mixing up historic and current fields
        // with the same name.
        return Table::column("current_" + colname);
    }
}
