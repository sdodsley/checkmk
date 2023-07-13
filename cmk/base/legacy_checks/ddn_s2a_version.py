#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


from cmk.base.check_api import LegacyCheckDefinition
from cmk.base.check_legacy_includes.ddn_s2a import parse_ddn_s2a_api_response
from cmk.base.config import check_info


def parse_ddn_s2a_version(info):
    return {key: value[0] for key, value in parse_ddn_s2a_api_response(info).items()}


def inventory_ddn_s2a_version(parsed):
    return [(None, None)]


def check_ddn_s2a_version(_no_item, _no_params, parsed):
    yield 0, "Platform: %s" % parsed["platform"]
    yield 0, "Firmware Version: %s (%s)" % (parsed["fw_version"], parsed["fw_date"])
    yield 0, "Bootrom Version: %s" % parsed["bootrom_version"]


check_info["ddn_s2a_version"] = LegacyCheckDefinition(
    parse_function=parse_ddn_s2a_version,
    service_name="DDN S2A Version",
    discovery_function=inventory_ddn_s2a_version,
    check_function=check_ddn_s2a_version,
)
