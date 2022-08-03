#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# fmt: off
# type: ignore

checkname = "fc_port"

info = [
    [
        u'1',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port0',
        u'7',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'2',
        u'8',
        u'2',
        u'3',
        u'2000000',
        u'port1',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 50, 32, 70, 49, 32, 67, 50, 32, 70,
            51
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 50, 32, 65, 54, 32, 69, 57, 32, 67,
            50
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 49, 51, 32, 57, 66, 32, 67, 50, 32, 69, 54, 32, 57,
            52
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 49, 50, 32, 65, 69, 32, 56, 57, 32, 49, 48, 32, 65,
            67
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            54
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'3',
        u'8',
        u'2',
        u'3',
        u'2000000',
        u'port2',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 52, 65, 32, 68, 50, 32, 49,
            68
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 49, 32, 51, 53, 32, 55, 52, 32, 52,
            55
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 49, 32, 55, 48, 32, 49, 55, 32, 48, 66, 32, 53,
            56
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 56, 32, 50, 57, 32, 51, 53, 32, 69, 56, 32, 69,
            56
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 50, 32, 51,
            65
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'4',
        u'8',
        u'2',
        u'3',
        u'2000000',
        u'port3',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 49, 32, 53, 51, 32, 49, 54, 32, 54,
            52
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 49, 32, 56, 53, 32, 54, 57, 32, 50,
            69
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 67, 70, 32, 56, 68, 32, 51, 57, 32, 48,
            67
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 56, 32, 70, 52, 32, 57, 69, 32, 65, 53, 32, 52,
            52
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 69,
            65
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'5',
        u'8',
        u'2',
        u'3',
        u'2000000',
        u'port4',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 51, 32, 52, 52, 32, 54, 56, 32, 65,
            65
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 50, 32, 70, 53, 32, 69, 68, 32, 56,
            54
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 52, 32, 70, 52, 32, 53, 48, 32, 51, 70, 32, 53,
            56
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 70, 32, 68, 69, 32, 68, 50, 32, 52, 50, 32, 69,
            56
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 54, 32, 54,
            53
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'6',
        u'8',
        u'2',
        u'3',
        u'2000000',
        u'port5',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 68, 65, 32, 56, 52, 32, 49,
            53
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 50, 32, 48, 70, 32, 70, 51, 32, 51,
            65
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 51, 32, 56, 56, 32, 56, 65, 32, 53, 52, 32, 49,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 69, 32, 70, 65, 32, 55, 67, 32, 55, 53, 32, 54,
            56
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 51, 32, 57,
            70
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'7',
        u'8',
        u'2',
        u'3',
        u'2000000',
        u'port6',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 53, 48, 32, 68, 65, 32, 50,
            51
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 51, 66, 32, 70, 54, 32, 51,
            68
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 49, 69, 32, 57, 49, 32, 67, 55, 32, 48,
            52
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 56, 68, 32, 49, 51, 32, 54, 70, 32, 70,
            67
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'8',
        u'8',
        u'2',
        u'3',
        u'2000000',
        u'port7',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 52, 66, 32, 48, 65, 32, 54,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 50, 69, 32, 66, 51, 32, 49,
            55
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 49, 68, 32, 52, 49, 32, 66, 67, 32, 51,
            56
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 51, 55, 32, 70, 67, 32, 65, 54, 32, 54,
            52
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            51
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'9',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port8',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'10',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port9',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'11',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port10',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'12',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port11',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'13',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port12',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'14',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port13',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'15',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port14',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'16',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port15',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'17',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port16',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'18',
        u'9',
        u'2',
        u'3',
        u'2000000',
        u'port17',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 50, 32, 50, 66, 32, 56, 54, 32, 57,
            52
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 53, 70, 32, 56, 65, 32, 66,
            69
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 49, 49, 32, 57, 66, 32, 54, 55, 32, 57, 56, 32, 56,
            67
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 54, 52, 32, 50, 50, 32, 56, 57, 32, 52,
            52
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 53, 32, 67, 68, 32, 50,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'19',
        u'9',
        u'2',
        u'3',
        u'2000000',
        u'port18',
        u'4',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 55, 32, 56, 52, 32, 49, 57, 32, 68,
            68
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 53, 32, 67, 56, 32, 52, 49, 32, 51,
            49
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 51, 49, 32, 68, 57, 32, 53, 49, 32, 53, 69, 32, 48,
            52
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 49, 68, 32, 54, 53, 32, 70, 65, 32, 48, 56, 32, 51,
            67
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 53, 32, 67, 68, 32, 50,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'20',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port19',
        u'7',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'21',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port20',
        u'7',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'22',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port21',
        u'7',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'23',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port22',
        u'7',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
    [
        u'24',
        u'10',
        u'3',
        u'9',
        u'2000000',
        u'port23',
        u'7',
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
        [
            48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48,
            48
        ],
    ],
]

discovery = {
    '': [
        ('01', 'fc_port_default_levels'),
        ('02', 'fc_port_default_levels'),
        ('03', 'fc_port_default_levels'),
        ('04', 'fc_port_default_levels'),
        ('05', 'fc_port_default_levels'),
        ('06', 'fc_port_default_levels'),
        ('07', 'fc_port_default_levels'),
        ('17', 'fc_port_default_levels'),
        ('18', 'fc_port_default_levels'),
    ],
}

DEFAULT_PARAMS = {
    "rxcrcs": (3.0, 20.0),  # allowed percentage of CRC errors
    "rxencoutframes": (3.0, 20.0),  # allowed percentage of Enc-OUT Frames
    "notxcredits": (3.0, 20.0),  # allowed percentage of No Tx Credits
    "c3discards": (3.0, 20.0),  # allowed percentage of C3 discards
}

checks = {
    '': [('01', DEFAULT_PARAMS, [
        (0, '16.0 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, online, ready, active, f-port', [
            ('in', 0.0, None, None, 0, 2000000000.0),
            ('out', 0.0, None, None, 0, 2000000000.0),
            ('rxobjects', 0.0),
            ('txobjects', 0.0),
            ('rxcrcs', 0.0),
            ('rxencoutframes', 0.0),
            ('c3discards', 0.0),
            ('notxcredits', 0.0),
        ]),
    ]),],
}
