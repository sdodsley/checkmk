#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# fmt: off
# type: ignore

checkname = 'dotnet_clrmemory'

info = [
    [
        u'AllocatedBytesPersec', u'Caption', u'Description', u'FinalizationSurvivors',
        u'Frequency_Object', u'Frequency_PerfTime', u'Frequency_Sys100NS', u'Gen0heapsize',
        u'Gen0PromotedBytesPerSec', u'Gen1heapsize', u'Gen1PromotedBytesPerSec', u'Gen2heapsize',
        u'LargeObjectHeapsize', u'Name', u'NumberBytesinallHeaps', u'NumberGCHandles',
        u'NumberGen0Collections', u'NumberGen1Collections', u'NumberGen2Collections',
        u'NumberInducedGC', u'NumberofPinnedObjects', u'NumberofSinkBlocksinuse',
        u'NumberTotalcommittedBytes', u'NumberTotalreservedBytes', u'PercentTimeinGC',
        u'PercentTimeinGC_Base', u'ProcessID', u'PromotedFinalizationMemoryfromGen0',
        u'PromotedMemoryfromGen0', u'PromotedMemoryfromGen1', u'Timestamp_Object',
        u'Timestamp_PerfTime', u'Timestamp_Sys100NS'
    ],
    [
        u'342508834992', u'', u'', u'3200', u'0', u'14318180', u'10000000', u'433175112',
        u'23101720', u'35139360', u'3347712', u'59379192', u'21526728', u'_Global_', u'116045280',
        u'40551', u'6458', u'2250', u'1302', u'86', u'110', u'8487', u'266633216', u'9663578112',
        u'175321424', u'-1', u'0', u'313116', u'23101720', u'3347712', u'0', u'18557575439465',
        u'131407216716290000'
    ],
    [
        u'70522792', u'', u'', u'253', u'0', u'14318180', u'10000000', u'29636664', u'633280',
        u'645880', u'3347712', u'4912856', u'939496', u'powershell', u'6498232', u'1064', u'4',
        u'2', u'1', u'0', u'8', u'30', u'27815936', u'402644992', u'273778', u'210388722', u'11700',
        u'41604', u'633280', u'3347712', u'0', u'18557575439465', u'131407216716290000'
    ],
    [
        u'0', u'', u'', u'0', u'0', u'14318180', u'10000000', u'0', u'0', u'0', u'0', u'0', u'0',
        u'SCNotification', u'0', u'365', u'0', u'0', u'0', u'0', u'0', u'37', u'0', u'0', u'0',
        u'0', u'0', u'0', u'0', u'0', u'0', u'18557575439465', u'131407216716290000'
    ],
    [
        u'9478053288', u'', u'', u'13', u'0', u'14318180', u'10000000', u'100150448', u'6174688',
        u'7077536', u'0', u'7438968', u'2334064', u'MonitoringHost', u'16850568', u'2266', u'439',
        u'219', u'126', u'28', u'36', u'166', u'33861632', u'402644992', u'228385', u'-198332580',
        u'30868', u'7012', u'6174688', u'0', u'0', u'18557575439465', u'131407216716290000'
    ],
    [
        u'124611739192', u'', u'', u'33', u'0', u'14318180', u'10000000', u'44739248', u'7674248',
        u'15068672', u'0', u'16361424', u'9782848', u'MonitoringHost#1', u'41212944', u'3651',
        u'3185', u'1021', u'808', u'28', u'1', u'945', u'97271808', u'402644992', u'766645',
        u'1836063', u'21848', u'15586', u'7674248', u'0', u'0', u'18557575439465',
        u'131407216716290000'
    ],
    [
        u'27953999208', u'', u'', u'104', u'0', u'14318180', u'10000000', u'44739248', u'7421464',
        u'10280056', u'0', u'7508048', u'3972640', u'MonitoringHost#2', u'21760744', u'3964',
        u'1401', u'566', u'275', u'29', u'36', u'371', u'48287744', u'402644992', u'381759',
        u'110984642', u'29996', u'9854', u'7421464', u'0', u'0', u'18557575439465',
        u'131407216716290000'
    ],
    [
        u'354055536', u'', u'', u'768', u'0', u'14318180', u'10000000', u'6291456', u'73960',
        u'132528', u'0', u'445736', u'74096', u'SQLAGENT', u'652360', u'2097', u'60', u'20', u'20',
        u'0', u'1', u'15', u'6934528', u'402644992', u'70', u'1290393684', u'6948', u'73728',
        u'73960', u'0', u'0', u'18557575439465', u'131407216716290000'
    ],
    [
        u'354071888', u'', u'', u'768', u'0', u'14318180', u'10000000', u'6291456', u'73960',
        u'132480', u'0', u'446704', u'74096', u'SQLAGENT#1', u'653280', u'2097', u'60', u'20',
        u'20', u'0', u'1', u'15', u'6934528', u'402644992', u'82', u'1290403265', u'6832', u'73728',
        u'73960', u'0', u'0', u'18557575439465', u'131407216716290000'
    ],
    [
        u'354063728', u'', u'', u'768', u'0', u'14318180', u'10000000', u'6291456', u'73960',
        u'132496', u'0', u'445736', u'74096', u'SQLAGENT#2', u'652328', u'2097', u'60', u'20',
        u'20', u'0', u'1', u'15', u'6934528', u'402644992', u'92', u'1290390403', u'6796', u'73728',
        u'73960', u'0', u'0', u'18557575439465', u'131407216716290000'
    ],
    [
        u'0', u'', u'', u'0', u'0', u'14318180', u'10000000', u'0', u'0', u'0', u'0', u'0', u'0',
        u'sqlservr', u'0', u'33', u'0', u'0', u'0', u'0', u'0', u'1', u'0', u'0', u'0', u'0', u'0',
        u'0', u'0', u'0', u'0', u'18557575439465', u'131407216716290000'
    ],
    [
        u'167995552', u'', u'', u'24', u'0', u'14318180', u'10000000', u'188743680', u'1272',
        u'1368', u'0', u'1521784', u'2260576', u'sqlservr#1', u'3783728', u'447', u'19', u'19',
        u'19', u'1', u'26', u'38', u'9170944', u'6442418176', u'33104', u'884734', u'428', u'768',
        u'1272', u'0', u'0', u'18557575439465', u'131407216716290000'
    ],
    [
        u'0', u'', u'', u'0', u'0', u'14318180', u'10000000', u'0', u'0', u'0', u'0', u'0', u'0',
        u'sqlservr#2', u'0', u'33', u'0', u'0', u'0', u'0', u'0', u'1', u'0', u'0', u'0', u'0',
        u'0', u'0', u'0', u'0', u'0', u'18557575439465', u'131407216716290000'
    ],
    [
        u'0', u'', u'', u'0', u'0', u'14318180', u'10000000', u'0', u'0', u'0', u'0', u'0', u'0',
        u'CcmExec', u'0', u'100', u'0', u'0', u'0', u'0', u'0', u'83', u'0', u'0', u'0', u'0', u'0',
        u'0', u'0', u'0', u'0', u'18557575439465', u'131407216716290000'
    ],
    [
        u'7909916312', u'', u'', u'469', u'0', u'14318180', u'10000000', u'6291456', u'974888',
        u'1668344', u'0', u'20297936', u'2014816', u'WmiPrvSE', u'23981096', u'22337', u'1230',
        u'363', u'13', u'0', u'0', u'6770', u'29421568', u'402644992', u'48875', u'689347', u'2708',
        u'17108', u'974888', u'0', u'0', u'18557575439465', u'131407216716290000'
    ]
]

discovery = {'': [(u'_Global_', 'dotnet_clrmemory_defaultlevels')]}

checks = {
    '': [
        (u'_Global_', {"upper": (10.0, 15.0)}, [
            (0, 'Time in GC: 4.08%', [
                ('percent', 4.082020000573718, 10.0, 15.0, 0, 100),
            ]),
        ]),
    ],
}
