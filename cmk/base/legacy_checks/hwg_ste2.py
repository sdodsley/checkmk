#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


from cmk.base.check_api import LegacyCheckDefinition
from cmk.base.check_legacy_includes.hwg import (
    check_hwg_humidity,
    check_hwg_temp,
    HWG_HUMIDITY_DEFAULTLEVELS,
    HWG_TEMP_DEFAULTLEVELS,
    inventory_hwg_humidity,
    inventory_hwg_temp,
    parse_hwg,
)
from cmk.base.config import check_info
from cmk.base.plugins.agent_based.agent_based_api.v1 import contains, SNMPTree

check_info["hwg_ste2"] = LegacyCheckDefinition(
    detect=contains(".1.3.6.1.2.1.1.1.0", "STE2"),
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.21796.4.9.3.1",
        oids=["1", "2", "3", "4", "7"],
    ),
    parse_function=parse_hwg,
    service_name="Temperature %s",
    discovery_function=inventory_hwg_temp,
    check_function=check_hwg_temp,
    check_ruleset_name="temperature",
    check_default_parameters=HWG_TEMP_DEFAULTLEVELS,
)


check_info["hwg_ste2.humidity"] = LegacyCheckDefinition(
    service_name="Humidity %s",
    discovery_function=inventory_hwg_humidity,
    check_function=check_hwg_humidity,
    check_ruleset_name="humidity",
    check_default_parameters=HWG_HUMIDITY_DEFAULTLEVELS,
)
