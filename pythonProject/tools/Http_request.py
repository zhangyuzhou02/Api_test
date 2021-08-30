import requests
from config.config import HOST
import logging
import json
class HttpRequest:
    def http_request(self,url,method,header,data=None,json=None):
        try:
            url =f'{HOST}'+url
            if method.upper()=='GET':
                logging.info("正在发送get请求，请求地址：{}， 请求参数{}".format(url))
                res = requests.get(url=url,data=data,headers=header,verify=False, allow_redirects=False)
            elif method.upper()=='POST':
                if json:
                    logging.info("正在发送请求，请求地址：{}， 请求参数{}".format(url, json))
                    res = requests.post(url=url,json=json,headers=header,verify=False, allow_redirects=False)
                else:
                    logging.info("正在发送请求，请求地址：{}， 请求参数{}".format(url, data))
                    res = requests.post(url=url,data=data,headers=header,verify=False, allow_redirects=False)
            else:
                logging.info("正在发送请求，请求地址：{}， 请求参数{}".format(url, data))
                print('请求方法不正确')
        except Exception as e:
            print("请求报错了：{0}".format(e))
            raise e
        return res

if __name__ == '__main__':
    url ='/api/community/app/post/search-of-home'
    method ="POST"
    header ={"Content-Type": "application/x-www-form-urlencoded","appaccesstoken": "604d8e0a9a8e6a1d05ef8cfc1f629ff47e5e2b45c1046a2c2b3c49a6bbe057e4aa92201e19ab7737b3b8f5c89e8187d762258ff7792483904a3cd8025831736fdaba82009e536e2425619ae2b6b08dfc5aac6671c47fbb0595437a200d60cca29b6535defd7d4abf1baf84b53b41408476a09d3d0e0e94bc660228cc630119e525"}
    data ={"success":"true","message":"获取成功","code":"0","value[0].id":"21","value[0].cityCode":"110100","value[0].tagIds":",4,19,5,20","value[0].name":"赛力斯大望京体验中心"}
    res = HttpRequest().http_request(url, method, header, json=data)
    print(res.json())
