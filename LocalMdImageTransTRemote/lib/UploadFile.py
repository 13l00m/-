from lib.OssSetting import getBucket,getprefixUploadname
from lib.config import PreDir
import time
import os
class UploadFile:
    def __init__(self):
        self.bucket = getBucket()
        self.predir = PreDir
        self.uploadStatus = {}
        self.prefixUploadname = getprefixUploadname()

    def getUploadName(self,localfilePath):
        if len(localfilePath.replace(" ",""))!=0:
            localfilePath = localfilePath.replace("\\","/")
            fileName = str(time.time()).split(".")[0]+"-"+localfilePath.split("/")[-1]
            remotePath = self.predir+"/"+fileName
            return remotePath
        else:
            return False

    def checkLocalFileExist(self,filePath):
        return os.path.isfile(filePath)

    def upload(self,localfilePaths):
        for filePath in localfilePaths:
            if self.checkLocalFileExist(filePath):
                try:
                    with open(filePath, 'rb') as fileobj:
                        remotePath = self.getUploadName(filePath)
                        try:
                            self.bucket.put_object(remotePath, fileobj)
                            self.uploadStatus[filePath] = {"remotePath": remotePath, "status": True, "des": "succ"}
                        except:
                            self.uploadStatus[filePath] = {"remotePath": remotePath, "status": False,"des": "OSS Upload File ERROR"}
                except:
                    pass
            else:
                self.uploadStatus[filePath] = {"remotePath":None,"status":False,"des":"File not Exists"}
