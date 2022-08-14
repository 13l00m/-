# -*- coding: utf-8 -*-
import oss2
import lib.config

auth = oss2.Auth(lib.config.AccessKeyId, lib.config.AccessKeySecret)
bucket = oss2.Bucket(auth, lib.config.endpoint, lib.config.Bucket)

def getBucket():
    return bucket

def getprefixUploadname():
    return "https://"+lib.config.Bucket+"."+lib.config.endpoint.split("://")[1]+"/"
