import os

import allure
import jsonpath
import pytest

from tools.Http_request import HttpRequest
from tools.Do_excel import Do_Excel

from config.config import header

global userId
test_data = Do_Excel().get_data('../data/buyer.xlsx', '社区')

class Test_run():
    @allure.feature('社区功能')
    @allure.story('发布验证')
    @allure.title('用例的标题')
    @allure.description('用例的描述')
    @allure.step("请求结果：{0}")
    @pytest.mark.parametrize('test_data',test_data)
    def test_run(self,test_data):
        for item in test_data:
            if eval(item['data']).find('${userId}') != -1:
                global userId
                item['data'] = item['data'].replace('${userId}', str(userId))
            else:
                item['data'] = item['data']
            res = HttpRequest().http_request(item['url'], item['method'], header, item['data'])
            res_json = res.json()
            print(res_json)
            if res_json['value'] != None:
                userId = jsonpath.jsonpath(res_json, "$.value.list[0].userId")[0]
        assert res_json['message'] == test_data['message']
        return res_json

if __name__ == '__main__':
# #--alluredir  生成allure报告需要的数据文件
    pytest.main(["test_run.py", "-sv", "--alluredir", "../report/tmp"])
    # allure generate 生成allure测试报告
    os.system("allure generate ../report/tmp -o ../report/report  --clean")
    # pytest -s -q --alluredir ['../report/tmp']

# pytest -s -q --alluredir=/Users/zhangyuzou/PycharmProjects/pythonProject/report/report /Users/zhangyuzou/PycharmProjects/pythonProject/test_case/test01.py
