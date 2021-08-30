from tools.Http_request import HttpRequest
from tools.Do_excel import Do_Excel

from config.config import header
import re


global_variables = {}
class Test:


    def run(self, url, method, data=None):
        if data != None:
            data = Test().resub_da(data)
            res = HttpRequest().http_request(url, method, header,data )
        else:
            res = HttpRequest().http_request(url, method, header)
        res_dict = res.json()
        # print('--------------',type(res_json))
        global_variables['key']=res_dict
        return res_dict


    def resub_da(self, data):
        results = re.findall(r'\$\{([^\{].+?)\}', data)
        if results != None:
            for result in results:
                if result == 'cloudToken':
                    value = header['appcloudtoken']
                    data = re.sub(r'\$\{' + result + '\}', str(value), data)
                elif result in global_variables['key']['value']['list'][0]:
                    value = global_variables['key']['value']['list'][0][result]
                    data = re.sub(r'\$\{' + result + '\}', str(value), data)
                else:
                    value = global_variables['key']['value'][result]
                    data = re.sub(r'\$\{' + result + '\}', str(value), data)
        return data

if __name__ == '__main__':
    test_data =Do_Excel().get_data('../data/app_api.xlsx','社区')
    for item in test_data:
        res = Test().run(item['url'],item['method'],item['data'])
        print(item['cheack'])
        # print(item['url'])
        # print(item['data'])
        print(res)

