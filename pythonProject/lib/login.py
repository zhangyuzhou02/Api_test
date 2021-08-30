import yaml
from config.config import HOST
import requests
class Login:
    def login(self,inData,mode = True):
        #url路径
        url = f'{HOST}/api/user/app/login/send-login-sms'
        #参数：
        payload = inData
        #请求：
        res = requests.post(url,json = inData)
        if mode:#获取token
            return res.json()['token']
        else:
            return res.json()
import  pprint
