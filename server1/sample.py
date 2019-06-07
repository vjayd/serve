#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:22:43 2019

@author: vijay
"""

import os
#os.mkdir("./dd")
result_file = open(os.path.join("./dd", "god"), 'r+')
result_file.write('File Name:')
result_file.truncate()