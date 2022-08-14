# -*- coding: utf-8 -*-

import re
import os
from  lib.OssSetting import getprefixUploadname
import lib.UploadFile

def collectImgUri(content):
    imageUriList = []
    image_arr = re.findall(r'(?:!\[(.*?)\]\((.*?)\))',content)
    for d in image_arr:
        imageUriList.append(d[1])
    return imageUriList

def replaceImageUri(uploadStatus,content):
    for filepath in uploadStatus:
        if uploadStatus[filepath]["status"]:
            content = content.replace(filepath,getprefixUploadname()+uploadStatus[filepath]["remotePath"])
    return content

def parseRes(res,content):
    for filepath in res:
        if res[filepath]['status']:
            print("[+]{} -> {} upload Succ".format(filepath,getprefixUploadname()+res[filepath]['remotePath']))
        else:
            print("[-]{} upload Fail\ndescribe:{}".format(filepath,res[filepath]['des']))

    File = open("out.md","w",encoding="UTF-8")
    File.write(content)
    File.close()
    print("[+] generate out file out.md")

def LocalImgTransToRemote(path):
    if os.path.isfile(path):
        content = open(path,"r",encoding="UTF-8").read()
        UriList = collectImgUri(content)
        upload = lib.UploadFile.UploadFile()
        upload.upload(UriList)
        content = replaceImageUri(upload.uploadStatus,content)
        parseRes(upload.uploadStatus,content)

    else:
        print(path+" not exists")