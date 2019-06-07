#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:46:52 2019

@author: vijay
"""

import requests
import sys
import random
import datetime




''' Server's base URL

8080
8081
8082
8083
8084

'''

a = random.randint(0,2)
#Create a random number based on that go to that url
def TimestampMillisec64(): 
	return float(( datetime .datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds())



if(a==0):
    BASE_URL = 'http://127.0.0.1:8080/' 
elif(a ==1):
    BASE_URL = 'http://127.0.0.1:8081/'
elif(a == 2):
    BASE_URL = 'http://127.0.0.1:8082/'

#Take in the argument from the terminal    
inputfile = sys.argv[1]
version = sys.argv[2]

#response
res = requests.post(BASE_URL + 'uploader',files={'file': open(inputfile, 'rb')},data ={'version':version,'timestamp': TimestampMillisec64()})  