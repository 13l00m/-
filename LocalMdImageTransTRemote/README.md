将本地本机更新到知识库或博客的过程中会浪费太多时间去做图片的搬运工，所以写了这个脚本，会将markdown文件中的图片转到云存储中并自动生成含远程图片的新md文件

添加阿里OSS JDK参考如下：  
https://help.aliyun.com/document_detail/85288.html  

用法：  
首先在lib.config中补全阿里云oss配置信息 
```
AccessKeyId = ""
AccessKeySecret = ""
Bucket = "" # 存储库名
endpoint = "" # 区域 如：https://oss-cn-hangzhou.aliyuncs.com

# 上传配置
PreDir = "" # 指定上传到oss的目录
```
在主程序(`main.py`)中替换md文件路径后执行`python3 main.py` 即可
