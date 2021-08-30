import pytest

from tools.yamControl import get_api_infos,get_cases_infos
from relse import  regex_sub
global_variables = {}
def run(client,casename):
    '''

    :param client: client = RequestsClient()的对象
    :param casename: 测试用例的名字
    :return:
    '''
    cases_info = get_api_infos(casename)  # {casename:[[接口1的信息],[接口2的信息]]}
    # steps = cases_info[casename]
    print(cases_info)
    for step in cases_info:
        # url 0, method 1,headers 索引值2，请求参数 索引值3，
        #响应提取 4，状态码断言 5，响应断言 6，数据库断言  7，用例参数 8
        # 字符串转换成字典的方法：'{"params":{\n"sku_id":891,\n"num":2\n}}'
        # 1.eval():可以将类似字典的字符串转换成字典 2.json.loads() 把json字符串转换成字典
        # eval()特点: 转换空字符串会报错，所以判空
        ####请求参数的处理#######
        # 1.url地址 ${变量} 变量替换
        url = step[0]
        client.url = regex_sub(url) # url做变量替换
        # 2.method
        method=step[1]
        client.method = method
        # 3.headers
        headers = step[2]
        if headers != '':
            # 先变量替换 然后做eval转换
            # 正则表达式是对字符串做处理
            client.headers = eval(regex_sub(headers))
        # 4.请求参数
        # 优先级处理: 如果测试用例有用例参数就用用例参数，否则就用默认参数
        if step[8] != '': # 用例参数有值
            params = regex_sub(step[8])  # 变量替换
        else:# 用api里面默认的参数
            params = regex_sub(step[3])  # 变量替换
        params = step[4]
        # 判断请求参数是什么类型：查询参数，data表单，file，json呢
        if 'params'in params:
            client.params = params['params'] # 查询参数
        if 'data' in params:
            client.data = params['data']
        if 'json' in params:
            client.json = params['json']
        if 'files' in params:
            client.data = params['files']
        ##########发起请求
        resp=client.send()
        ######## 获取响应了，断言处理
        # 响应提取 4，状态码断言 5，响应断言 6，数据库断言  7，
        # 5.数据提取
        extract_data = step[4]
        if extract_data !='': # '{"buyerToken":"$.access_token"\n}'
            extract_data = eval(extract_data)  # 字符串转字典
            for item in extract_data.items():# item 是(key,value)
                key = item[0]  # 数据提取赋值的变量
                jsonpath_value = item[1]   # jsonpath的表达式
                # 解析jsonpath表达式
                value = client.extract_expr(jsonpath_value)
                # 把响应数据里面提取出的变量和值存储到全局变量global_variables
                global_variables[key]=value
        # 6.状态码断言
        expect_status_code = step[5]
        if expect_status_code != '':
            # 断言  pytest.assume(表达式)
            pytest.assume(resp.status_code==expect_status_code)
        # 7.响应断言 # '{"actual":"$.message", "expect":"购买数量不能为空"}'
        expect_body_assert = step[6]
        if expect_body_assert != '':
            expect_body_assert=eval(expect_body_assert)
            jsonpath_value = expect_body_assert['actual']  # jsonpath表达式
            # 解析jsonpath表达式
            actual_value = client.extract_expr(jsonpath_value)
            expect_value = expect_body_assert["expect"]
            pytest.assume(actual_value==expect_value)

if __name__ == '__main__':
    client = RequestsClient()
    run(client,'立即购买')
