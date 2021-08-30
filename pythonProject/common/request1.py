from config.config import HOST
import requests
class Request:
    def post(self,url,inData,mode = True):
        #url路径
        #参数：
        payload = inData
        #请求：
        if inData=='json':
            res = requests.post(url,json = inData)
        res = requests.post(url, data=inData)
        if mode:#获取token
            return res.json()['token']
        else:
            return res.json()