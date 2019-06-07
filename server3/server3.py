#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:58:04 2019

@author: vijay
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:50:02 2019

@author: vijay
"""
import requests
from random import randint 
from Crypto import Random 
from Crypto.Cipher import AES 
from flask import Flask, render_template, request

from werkzeug import secure_filename
import base64 
import hashlib 
import os 
import time 
import datetime 
from werkzeug import secure_filename
from Crypto import Random  
from Crypto.Cipher import AES 
from flask import Flask , jsonify , request 






app = Flask(__name__) 

BASE_URL_S1 = 'http://127.0.0.1:8080/' 
BASE_URL_S2 = 'http://127.0.0.1:8081/' 
UPLOAD_FOLDER = './'



def write_check(filename, version, timestampattached):
    f=open("god", "r")
    f1 = f.readlines()
    exist = False
    for x in f1:
        splitted = x.split(";")
        print(splitted)
        name = splitted[0].split(":")
        versin = splitted[1].split(":")
        timestamp = splitted[2].split(":")
        if(name[1] == filename and versin[1].strip() == version):
            if(float(timestamp[1])<timestampattached):
                exist = True
                break
    if (exist):
        return True
    else:
        result_file = open('god', 'a+')
        timestamp = TimestampMillisec64()
        result_file.write('File Name:'+filename+'; version :'+version+'; timestamp :'+str(timestamp)+'\n') 
        
        return False



def TimestampMillisec64(): 
	return float(( datetime .datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds())




def makecopies(f, version, timestampattached):
    res1 = requests.post(BASE_URL_S2 + 'uploader',files={'file': open(f, 'rb')}, data = {'version':version,'timestamp': timestampattached})  
    res2 = requests.post(BASE_URL_S2 + 'uploader',files={'file': open(f, 'rb')}, data = {'version':version,'timestamp': TimestampMillisec64()})
    return res1, res2


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      payload = request.form
      version = payload['version']
      filename = secure_filename(f.filename)
      timestampattached = TimestampMillisec64()
      var = write_check(filename, version, timestampattached)
      if (var):
          return jsonify({ 'file': filename , 'version': version, "var":var})
      else:
          f.save(os.path.join(UPLOAD_FOLDER, filename))
          res1, res2 = makecopies(f, version, timestampattached)
          return jsonify({ 'file': filename , 'version': version, "var":var})


if __name__ == '__main__': 
	app.run(host='0.0.0.0', debug=True, port=8082)
