#! /usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright © 2017 laineyluo      Huazhong university of Science and Technology
#
# Distributed under terms of the MIT license


"""anamoly detection model and training configurations"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path as osp

LOG_DIR = '~/anomaly-detection/logs' # where checkpoints, logs are saved
RUN_NAME = 'test' # identifier of experiments
BATCH_SIZE = 32 # training batch size

@ex.config
def configurations():
  model_config = {
    'seed': 0,

    ### Input config
    # input csv database file path
    # must be provided in training modes.
    'prefetch_config': {'input_csv':'/home/luohuifen/anomaly-detection/data/itraffic_data_per_hourly.csv',
                        'csv_col_names':['Time','ISP']
                        'output_log': osp.join(LOG_DIR, 'model_checkpoints', RUN_NAME),
                        'batch_size': BATCH_SIZE
                         }}

