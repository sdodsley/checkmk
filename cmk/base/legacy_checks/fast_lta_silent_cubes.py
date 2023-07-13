#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


from cmk.base.check_api import LegacyCheckDefinition
from cmk.base.check_legacy_includes.df import df_check_filesystem_list, FILESYSTEM_DEFAULT_PARAMS
from cmk.base.config import check_info
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
    all_of,
    any_of,
    exists,
    SNMPTree,
    startswith,
)


def inventory_fast_lta_silent_cubes_status(info):
    if len(info) > 0 and len(info[0]) > 1:
        return [("Total", {})]
    return []


def check_fast_lta_silent_cubes_status(item, params, info):
    fslist = []
    for total, used in info:
        size_mb = int(total) / 1048576.0
        avail_mb = (int(total) - int(used)) / 1048576.0
        fslist.append((item, size_mb, avail_mb, 0))

    return df_check_filesystem_list(item, params, fslist)


check_info["fast_lta_silent_cubes"] = LegacyCheckDefinition(
    detect=all_of(
        startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.8072.3.2.10"),
        any_of(
            exists(".1.3.6.1.4.1.27417.3.2"),
            exists(".1.3.6.1.4.1.27417.3.2.0"),
        ),
    ),
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.27417.3",
        oids=["2", "3"],
    ),
)


check_info["fast_lta_silent_cubes.capacity"] = LegacyCheckDefinition(
    service_name="Fast LTA SC Capacity %s",
    discovery_function=inventory_fast_lta_silent_cubes_status,
    check_function=check_fast_lta_silent_cubes_status,
    check_ruleset_name="filesystem",
    check_default_parameters=FILESYSTEM_DEFAULT_PARAMS,
)
