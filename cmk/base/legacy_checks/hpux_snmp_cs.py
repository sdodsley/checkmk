#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# Some relevant OIDs are
# sysUpTime: 1.3.6.1.4.1.11.2.3.1.1.1
# sysUsers: 1.3.6.1.4.1.11.2.3.1.1.2
# sysAvgJobs1: 1.3.6.1.4.1.11.2.3.1.1.3
# sysAvgJobs5: 1.3.6.1.4.1.11.2.3.1.1.4
# sysAvgJobs15: 1.3.6.1.4.1.11.2.3.1.1.5
# sysMaxProcess: 1.3.6.1.4.1.11.2.3.1.1.6
# sysFreeMemory: 1.3.6.1.4.1.11.2.3.1.1.7
# sysPhysMemory: 1.3.6.1.4.1.11.2.3.1.1.8
# sysMaxUserMemory: 1.3.6.1.4.1.11.2.3.1.1.9
# sysSwapConfig: 1.3.6.1.4.1.11.2.3.1.1.10
# sysEnabledSwap: 1.3.6.1.4.1.11.2.3.1.1.11
# sysFreeSwap: 1.3.6.1.4.1.11.2.3.1.1.12
# sysUserCPU: 1.3.6.1.4.1.11.2.3.1.1.13
# sysSysCPU: 1.3.6.1.4.1.11.2.3.1.1.14
# sysIdleCPU: 1.3.6.1.4.1.11.2.3.1.1.15
# sysNiceCPU: 1.3.6.1.4.1.11.2.3.1.1.16

# Example walk:
# .1.3.6.1.4.1.11.2.3.1.1.1.0  215207600
# .1.3.6.1.4.1.11.2.3.1.1.10.0  33357824
# .1.3.6.1.4.1.11.2.3.1.1.11.0  33357824
# .1.3.6.1.4.1.11.2.3.1.1.12.0  29350932
# .1.3.6.1.4.1.11.2.3.1.1.13.0  52129100
# .1.3.6.1.4.1.11.2.3.1.1.14.0  23331438
# .1.3.6.1.4.1.11.2.3.1.1.15.0  123137168
# .1.3.6.1.4.1.11.2.3.1.1.16.0  10


import time

from cmk.base.check_api import get_rate, LegacyCheckDefinition
from cmk.base.config import check_info
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
    IgnoreResultsError,
    OIDEnd,
    SNMPTree,
    startswith,
)


def inventory_hpux_snmp_cpu(info):
    if len(info) > 0:
        return [(None, None)]
    return []


def check_hpux_snmp_cpu(item, _no_params, info):
    parts = dict(info)
    this_time = time.time()
    total_rate = 0.0
    rates = []
    for what, oid in [("user", "13.0"), ("system", "14.0"), ("idle", "15.0"), ("nice", "16.0")]:
        value = int(parts[oid])
        rate = get_rate("snmp_cpu_util.%s" % what, this_time, value)
        total_rate += rate
        rates.append(rate)

    if total_rate == 0:
        raise IgnoreResultsError("No counter counted. Time has ceased to flow.")

    perfdata = []
    infos = []
    for what, rate in zip(["user", "system", "idle", "nice"], rates):
        part = rate / total_rate  # fixed: true-division
        perc = part * 100
        perfdata.append((what, perc, None, None, 0, 100))
        infos.append("%s: %.0f%%" % (what, perc))

    return (0, ", ".join(infos), perfdata)


check_info["hpux_snmp_cs"] = LegacyCheckDefinition(
    detect=startswith(".1.3.6.1.2.1.1.1.0", "HP-UX"),
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.11.2.3.1",
        oids=[OIDEnd(), "1"],
    ),
)


check_info["hpux_snmp_cs.cpu"] = LegacyCheckDefinition(
    service_name="CPU utilization",
    discovery_function=inventory_hpux_snmp_cpu,
    check_function=check_hpux_snmp_cpu,
)
