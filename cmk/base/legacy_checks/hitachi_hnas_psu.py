#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


from cmk.base.check_api import LegacyCheckDefinition
from cmk.base.config import check_info
from cmk.base.plugins.agent_based.agent_based_api.v1 import SNMPTree
from cmk.base.plugins.agent_based.utils.hitachi_hnas import DETECT


def inventory_hitachi_hnas_psu(info):
    inventory = []
    for clusternode, id_, _status in info:
        inventory.append((clusternode + "." + id_, None))
    return inventory


def check_hitachi_hnas_psu(item, _no_params, info):
    statusmap = (
        ("", 3),  # 0
        ("ok", 0),  # 1
        ("failed", 2),  # 2
        ("notFitted", 1),  # 3
        ("unknown", 3),  # 4
    )

    for clusternode, id_, status in info:
        if clusternode + "." + id_ == item:
            status = int(status)
            if status == 0 or status >= len(statusmap):
                return 3, "PNode %s PSU %s reports unidentified status %s" % (
                    clusternode,
                    id_,
                    status,
                )
            return statusmap[status][1], "PNode %s PSU %s reports status %s" % (
                clusternode,
                id_,
                statusmap[status][0],
            )

    return 3, "SNMP did not report a status of this PSU"


check_info["hitachi_hnas_psu"] = LegacyCheckDefinition(
    detect=DETECT,
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.11096.6.1.1.1.2.1.13.1",
        oids=["1", "2", "3"],
    ),
    service_name="PSU %s",
    discovery_function=inventory_hitachi_hnas_psu,
    check_function=check_hitachi_hnas_psu,
)
