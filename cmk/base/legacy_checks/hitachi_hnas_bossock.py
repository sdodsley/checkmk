#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


from cmk.base.check_api import LegacyCheckDefinition
from cmk.base.config import check_info
from cmk.base.plugins.agent_based.agent_based_api.v1 import SNMPTree
from cmk.base.plugins.agent_based.utils.hitachi_hnas import DETECT

hitachi_hnas_bossock_default_levels = (250, 350)


def inventory_hitachi_hnas_bossock(info):
    for clusternode, _fibers in info:
        yield clusternode, hitachi_hnas_bossock_default_levels


def check_hitachi_hnas_bossock(item, params, info):
    for clusternode, fibers in info:
        if clusternode == item:
            warn, crit = params
            infotext = "%s running (levels %d/%d)" % (fibers, warn, crit)

            if int(fibers) >= crit:
                state = 2
            elif int(fibers) >= warn:
                state = 1
            else:
                state = 0

            perfdata = [("fibers", fibers, warn, crit)]

            return state, infotext, perfdata
    return None


check_info["hitachi_hnas_bossock"] = LegacyCheckDefinition(
    detect=DETECT,
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.11096.6.1.1.6.7.4.1",
        oids=["1", "2"],
    ),
    service_name="Bossock Fibers on Node %s",
    discovery_function=inventory_hitachi_hnas_bossock,
    check_function=check_hitachi_hnas_bossock,
    check_ruleset_name="bossock_fibers",
)
