#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


# <<<db2_counters>>>
# TIMESTAMP 1426610723
# db2taddm:CMDBS1 deadlocks 0
# db2taddm:CMDBS1 lockwaits 99
# db2taddm:CMDBS1 sortoverflows 2387
# TIMESTAMP 1426610763
# db2taddm:CMDBS6 deadlocks 99
# db2taddm:CMDBS6 lockwaits 91
# db2taddm:CMDBS6 sortoverflows 237
#### Example for database in DPF mode
# TIMESTAMP 1439976757
# db2ifa:DDST1 node 0 iasv0091 0
# db2ifa:DDST1 node 1 iasv0091 1
# db2ifa:DDST1 node 2 iasv0091 2
# db2ifa:DDST1 node 3 iasv0091 3
# db2ifa:DDST1 node 4 iasv0091 4
# db2ifa:DDST1 node 5 iasv0091 5
# db2ifa:DDST1 deadlocks 0
# db2ifa:DDST1 deadlocks 0
# db2ifa:DDST1 deadlocks 0
# db2ifa:DDST1 deadlocks 0
# db2ifa:DDST1 deadlocks 0
# db2ifa:DDST1 deadlocks 0
# db2ifa:DDST1 lockwaits 0
# db2ifa:DDST1 lockwaits 0
# db2ifa:DDST1 lockwaits 0
# db2ifa:DDST1 lockwaits 0
# db2ifa:DDST1 lockwaits 0
# db2ifa:DDST1 lockwaits 80


# mypy: disable-error-code="var-annotated"

from cmk.base.check_api import get_rate, LegacyCheckDefinition, RAISE
from cmk.base.config import check_info
from cmk.base.plugins.agent_based.agent_based_api.v1 import IgnoreResultsError

db2_counters_map = {
    "deadlocks": "Deadlocks",
    "lockwaits": "Lockwaits",
}


def parse_db2_counters(info):
    dbs = {}
    timestamp = 0
    node_infos = []
    element_offset = {}
    for line in info:
        if line[0].startswith("TIMESTAMP"):
            element_offset = {}
            node_infos = []
            timestamp = int(line[1])
        elif line[1] == "node":
            node_infos.append(" ".join(line[2:]))
        # Some databases run in DPF mode. Means that the database is split over several nodes
        # The counter information also differs for each node. We create one service per DPF node
        elif line[1] in db2_counters_map:
            if node_infos:
                element_offset.setdefault(line[1], 0)
                offset = element_offset[line[1]]
                key = "%s DPF %s" % (line[0], node_infos[offset])
                element_offset[line[1]] += 1
            else:
                key = line[0]
            dbs.setdefault(key, {"TIMESTAMP": timestamp})
            dbs[key][line[1]] = line[2]

    # The timestamp is still used for legacy reasons
    # The instance specific timestamp is now available in the dbs
    return timestamp, dbs


def inventory_db2_counters(parsed):
    if len(parsed) == 2:
        for db in parsed[1]:
            yield db, {}


def check_db2_counters(item, params, parsed):
    default_timestamp = parsed[0]
    db = parsed[1].get(item)
    if not db:
        raise IgnoreResultsError("Login into database failed")

    wrapped = False
    timestamp = db.get("TIMESTAMP", default_timestamp)
    for counter, label in db2_counters_map.items():
        try:
            value = float(db[counter])
        except ValueError:
            yield 2, "Invalid value: " + db[counter]
            continue

        try:
            rate = get_rate("db2_counters.%s.%s" % (item, counter), timestamp, value, onwrap=RAISE)
        except IgnoreResultsError:
            wrapped = True
            continue

        warn, crit = params.get(counter, (None, None))
        perfdata = [(counter, rate, warn, crit)]
        if crit is not None and rate >= crit:
            yield 2, "%s: %.1f/s" % (label, rate), perfdata
        elif warn is not None and rate >= warn:
            yield 1, "%s: %.1f/s" % (label, rate), perfdata
        else:
            yield 0, "%s: %.1f/s" % (label, rate), perfdata

    if wrapped:
        raise IgnoreResultsError("Some counter(s) wrapped, no data this time")


check_info["db2_counters"] = LegacyCheckDefinition(
    parse_function=parse_db2_counters,
    service_name="DB2 Counters %s",
    discovery_function=inventory_db2_counters,
    check_function=check_db2_counters,
    check_ruleset_name="db2_counters",
    check_default_parameters={},
)
