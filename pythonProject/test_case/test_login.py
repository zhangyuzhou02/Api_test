

#1执行用例
#获取数据
# from tools.yancon import get_yam_data
# res = get_yam_data("../data/loginCase.yaml")[1]['data']
# #调用接口
# resdata = login().login(res,False)
#判断断言

#批量执行用例

#引入框架pytest
import pytest

from common.run import Test
import allure,os
#登录接口-测试类封装
#多个用例需要运行，数据驱动-读取用例数据
from tools.Do_excel import Do_Excel

test_data =Do_Excel().get_data('../data/buyer.xlsx','社区')

class Test_login:

    @allure.feature('社区功能')
    @allure.story('发布验证')
    # @allure.title('用例的标题')
    @allure.description('用例的描述')
    @pytest.mark.parametrize('url',test_data)
    def test_login(self,url):
        res = Test().run(test_data)
        # res = Test().run(test_data)
        # print(res.status_code)
        # print(res.json())
        # assert res['message'] == test_data['message']
        pytest.assume(res.message == test_data['message'])


if __name__ == '__main__':
#     # #--alluredir  生成allure报告需要的数据文件
#     pytest.main(["test_login.py", "-sv", "--alluredir", "../report/tmp"])
#     # allure generate 生成allure测试报告
#     os.system("allure generate ../report/tmp -o ../report/report  --clean")

    pytest.main(["--alluredir", "report/result", "test_login.py"])
    split ='allure'+'generate'+'./report/result'+'-o'+'./report/html'+'--clean'
    # allure generate 生成allure测试报告
    os.system(split)





