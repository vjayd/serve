#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:58:12 2019

@author: vijay
"""
import sys


def write_check(filename, version):
    f=open("god", "r")
    f1 = f.readlines()
    exist = False
    for x in f1:
        splitted = x.split(";")
        name = splitted[0].split(":")
        versin = splitted[1].split(":")
        
        if(name[1] == filename and versin[1].strip() == version):
            
            exist = True
            break
    if (exist):
        return True
    else:
        result_file = open('god', 'a+')
        result_file.write('File Name:'+filename+'; version :'+version+'\n') 
        return False

#filename = sys.argv[1]
#version = sys.argv[2]

#var = write_check(filename, version)

#if(var):
#    print("File already exists with version :"+version)
#else:
#    print("Successfully updated")