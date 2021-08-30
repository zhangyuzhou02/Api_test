import logging
import requests
from requests import Session
from tools.yancon import get_yam_data
import Relse
global_variables = {}
class MyRequest:
    def sendRequest(self, url, method, appaccesstoken,params=None, data=None,
                    headers=None, json=None, ):

        headers = {"Content-Type": "application/x-www-form-urlencoded","appaccesstoken": appaccesstoken}
        results = Relse.findall(r'\$\{([^\{].+?)\}', data)
        # if data：
        responseResult = None
        new_method = method.lower()
        if new_method == 'get':
            logging.info("正在发送get请求，请求地址：{}， 请求参数{}".format(url, params))
            responseResult = requests.get(url=url, params=params, headers=headers)
            global_variables[global_variables]=responseResult
        elif new_method == "post":
            if json:
                logging.info("正在发送请求，请求地址：{}， 请求参数{}".format(url, json))
                responseResult = requests.post(url=url, json=json, headers=headers)
            else:
                logging.info("正在发送请求，请求地址：{}， 请求参数{}".format(url, data))
                responseResult = requests.post(url=url, data=data, headers=headers)
        return responseResult.json()
if __name__ == '__main__':
    print(get_yam_data('../data/Case.yaml'))

