#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:17:49 2019

@author: vijay
"""

import json
import pingparsing

ping_parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()
transmitter.destination = "10.100.11.13"
transmitter.count = 10
result = transmitter.ping()
result = ping_parser.parse(result).as_dict()


#print(result['rtt_avg'])
print(result)
#datastore = json.loads(result)
    #print(json.dumps(ping_parser.parse(result).as_dict(), indent=4))