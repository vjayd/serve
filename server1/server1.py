#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:50:02 2019

@author: vijay
"""

from random import randint 
from Crypto import Random 
from Crypto.Cipher import AES 
from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename

import os 
import requests
import datetime



app = Flask(__name__) 


BASE_URL_S2 = 'http://127.0.0.1:8081/' 
BASE_URL_S3 = 'http://127.0.0.1:8082/' 
BASE_URL_S4 = 'http://127.0.0.1:8083/' 
BASE_URL_S5 = 'http://127.0.0.1:8084/' 
GOD ='./'
UPLOAD_FOLDER = './'

#creates timestamp to be attached to the request
def TimestampMillisec64(): 
	return float(( datetime .datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds())


#for writing a file to specific folder
def write_check(f, filename, version, timestampattached):
    dirname = './' + filename
    
    if(os.path.isdir(dirname)):
        newfile = filename + str(fcount(dirname))
        result_file = open(os.path.join(dirname, "god"), 'r+')
           
        exist = False
        x= result_file.readline()
        splitted = x.split(";")
        name = splitted[0].split(":")
        versin = splitted[1].split(":")
        timestamp = splitted[2].split(":")
           
        	
            #if the updated request is having minimum timestamp reject the received request
        if(float(timestamp[1])<timestampattached):
            if(name[1] == filename and versin[1].strip() == version):
                exist = True
                return version, exist
            else:
                result_file = open(os.path.join(dirname, "god"), 'w+')
                result_file.write('File Name:'+filename+'; version :'+version+'; timestamp :'+str(timestampattached))
                result_file.truncate()
                f.save(os.path.join(dirname, newfile))
                return version, exist
            #if the updated request is having greater timestamp then the received request :(1)update the received request file in place of existing file (2)update the entry in god file correspondinng to the received request 	   		
        else:
				#here we want to update the timestamp field in god file 
            result_file = open(os.path.join(dirname, "god"), 'w+')
            result_file.write('File Name:'+filename+'; version :'+version+'; timestamp :'+str(timestampattached))
            result_file.truncate()
            f.save(os.path.join(dirname, newfile))
            return version, exist   #if the directory does not exist with filename in the path : (1)create the directory and add the file into the folder (2)add entry into the god file
    else:
        exist = False
        os.mkdir(dirname)
        result_file = open(os.path.join(dirname, "god"), 'w+')
        newfile = filename + str(fcount(dirname))
        result_file.write('File Name:'+filename+'; version :'+version+'; timestamp :'+str(timestampattached))
        result_file.truncate()
        f.save(os.path.join(dirname, newfile))
        return version, exist
 
    
#counting number of files in specified path  
def fcount(path):
    #Counts the number of files in a directory
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1

    return count

def makecopies(f, version, timestampattached):
    res1 = requests.post(BASE_URL_S2 + 'uploader',files={'file': open(f, 'rb')}, data ={'version':version,'timestamp': timestampattached})  
    res2 = requests.post(BASE_URL_S3 + 'uploader',files={'file': open(f, 'rb')}, data ={'version':version,'timestamp': timestampattached})
    return res1, res2
    

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      payload = request.form
      version = payload['version']
      filename = secure_filename(f.filename)
      timestampattached = TimestampMillisec64()
      version, ex = write_check(f, filename, version, timestampattached)
      
      return jsonify({'file': filename , 'version': version, 'exist':ex})
      





if __name__ == '__main__': 
	app.run(host='0.0.0.0', debug=True, port=8080)
    
