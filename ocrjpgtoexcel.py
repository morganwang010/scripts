# coding:utf-8
import urllib, urllib2, base64,json

import urllib, urllib2, sys
import ssl
ApiKey = 'qEsdNlAGRrO94iY1wZ0XHFVS'
SecKey = '5rcxuolbg1dv4xG3gGqrdo7MiMId3STL'
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+ApiKey+ '&client_secret='+SecKey
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)

#access_token = '#####调用鉴权接口获取的token#####'
access_token = response.read()
token = json.loads(access_token)
print(token["access_token"])
 
 





urlocr = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request?access_token=' + str(token["access_token"])
print(urlocr)
# 二进制方式打开图文件
f = open(r'aa-82_1.jpg', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img}
params = urllib.urlencode(params)
request = urllib2.Request(urlocr, params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
ocrResult = response.read()
print(ocrResult)
r = json.loads(ocrResult)
print(r.keys())
rid = r["result"][0]["request_id"]


print(rid)

#取回结果

getUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result?access_token='+str(token["access_token"])

params1 = {"request_id": rid,"result_type": "excel"}
params1 = urllib.urlencode(params1)
request1 = urllib2.Request(urlocr, params1)
request1.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request1)
rUrl = response.read()
print(rUrl)