import os
import sys

import allure
import pytest
sys.path.append("/Users/zhangyuzou/PycharmProjects/pythonProject")
from tools.Do_excel import Do_Excel
from common.run import Test
from config.config import header

# @allure.feature('发布模块')
class Test_run1():
    test_data = Do_Excel().get_data('../data/app_api.xlsx', '社区')
    data1 =[]
    for item in test_data:
        dict = {}
        dict['url']=item['url']
        dict['data'] = item['data']
        dict['method'] = item['method']
        dict['cheack'] = item['cheack']
        data1.append(dict.values())

    @allure.epic('APP接口测试')
    @allure.story('发布接口')
    @allure.description('用例的描述:{}')
    @allure.feature('测试功能')
    @allure.title('测试模块')
    @pytest.mark.parametrize("url,data,method,cheack",data1)
    def test_run(self,url,data,method,cheack):
        allure.dynamic.description('{}接口'.format(cheack))
        allure.dynamic.title('{}接口'.format(cheack))
        res = Test().run(url,method,data)
        with allure.step('接口请求url'):
            allure.attach('{}'.format(url), name='请求url')
        with allure.step('接口请求参数'):
            allure.attach('{}'.format(data), name='请求参数')
        with allure.step('接口请求header'):
            allure.attach('{}'.format(header), name='请求header')
        with allure.step('接口返回结果'):
            allure.attach('{}'.format(res['success']), name='返回结果')
        with allure.step('接口返回message'):
            allure.attach('{}'.format(res['message']), name='返回message')
        with allure.step('接口返回code'):
            allure.attach('{}'.format(res['code']), name='返回code')
        with allure.step('接口返回value'):
            allure.attach('{}'.format(res['value']), name='返回value')
        # print(res['success'])
        # print(item['message'])
        assert res['success'] == True

if __name__ == '__main__':
# #--alluredir  生成allure报告需要的数据文件
    pytest.main(["test01.py", "-sv", "--alluredir", "../report/tmp"])
    # allure generate 生成allure测试报告
    os.system("allure generate ../report/tmp -o ../report/report  --clean")

