#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:01:55 2019

@author: vijay
"""

import requests
import sys
import datetime
from subprocess import Popen, PIPE, STDOUT
from pythonping import ping
import pingparsing


'''Get average round trip time for a given host'''
def get_ping_time(host):
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = host
    transmitter.count = 10
    result = transmitter.ping()
    result = ping_parser.parse(result).as_dict()
    return result['rtt_avg']


'''functin to create a timestamp'''
def TimestampMillisec64(): 
	return float(( datetime .datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds())


''' functtion to return the nearest server by averaging the roundtrip time'''
def nearestserver():
    
    timedict = {}

    s1 = get_ping_time("10.100.11.13")
    s2 = get_ping_time("10.100.11.27")
    s3 = get_ping_time("10.100.11.35")
 
    timedict[s1] = 0
    timedict[s2] = 1
    timedict[s3] = 2

    men = min(timedict, key=timedict.get)
    minserver = timedict[men]
    return minserver


'''If there are no physical systems connected , then we will use server1 as the nearest server'''
a = 0
if(a==0):
    BASE_URL = 'http://127.0.0.1:8080/' 
elif(a ==1):
    BASE_URL = 'http://127.0.0.1:8081/'
elif(a == 2):
    BASE_URL = 'http://127.0.0.1:8082/'
    
    

''' Take in the request from the user and return the appropriate response from the server'''
#inputfile = sys.argv[1]
#version = sys.argv[2]

inputfile = './thesisfilesssss'
version = 2

res2 = requests.post(BASE_URL + 'uploader',files={'file': open(inputfile, 'rb')},data ={'version':version})   
res = res2.json()
if(res['exist']):
    print("This version already exists , the latest version is :"+res['version'])
else:
    print("The version of this file successfully updated")

