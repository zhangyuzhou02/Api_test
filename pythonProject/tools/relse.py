
import re
# 替换变量
# 1.检索那个位置用到了变量的引用
# 2.替换变量:global_variables
def regex_sub(string):
    '''
${buyerHost}- buyerHost-global_variables对应的真实的值-替换${buyerHost}=http://www.mtxshop.com:7002
    :param string: '${buyerHost}/passport/login'
    :return:
    '''
    # re.findall(pattern,string)
    # pattern 正则表达式的规则  目标字符串
    # 在string这个字符串中进行检索，看是否有符合pattern正则表达式的部分，如果有就返回，没有即返回None
    # findall如果有值的话，返回的是[符合规则的值，xxx]
    # $ 以什么结尾是特殊的正则表达式，匹配的${} 这个$并没有特殊函数 \转义的意思
    # results = re.findall(r'\$\{(.+?)\}',"${{md5(yaoyao123456)}}")
    results = re.findall(r'\$\{([^\{].+?)\}', string)
    for result in results:
        # buyerHost这个变量所代表的真实的值是什么？
        # global_variables里面去找
        # value = global_variables[result]
        # print('value的值是{}'.format(value))
        # 做替换${buyerHost}-'http://www.mtxshop.com:7002'
        # pattern:这个规则可以把你想要替换掉的内容匹配出来
        # string =re.sub(r'\$\{'+result+'\}',value,string)
        # print(type(dict))
        # print(str(dict[result]))
        value = global_variables[result]
        print(value['value']['list'][0]['result'])
        string = re.sub(r'\$\{' + result + '\}', str(value['value']['list'][0]['result']), string)
    return string

if __name__ == '__main__':
    global_variables={}
    # string1 = {'success': True, 'message': '获取成功', 'code': '0',
    #  'value': {'hasMore': True, 'list': [{'userId': 104, 'userImageKey': 'i'}]}}
    string1 = {
	"success": True,
	"message": "获取成功",
	"code": "0",
	"value": {
		"userImageKey": "images/2021/3/c49b259a937d401bb34273f7d31b9bb7.jpg",
		"userNickname": "撒打发就阿斯蒂芬就阿三就阿里快",
		"userVerified": False,
		"subscribed": False,
		"userVerifyType": 0,
		"userId": 60,
		"type": 0,
		"postId": 578}}
    str2 = {'success': True,
            'message': '获取成功',
            'code': '0',
            'value': {'hasMore': True, 'list':
                [{'userId': 6, 'userImageKey': 'images/2021/2/d874bec7683f4c7c99fb9b83e0c3604d.jpg',
                  'userNickname': 'leoleoleol大神大多eoleoleole阿', 'userVerified': False,
                  'subscribed': True, 'userVerifyType': 2, 'type': 1, 'postId': 117,}]}}
    str3 = {'key':
                {'success': True, 'message': '获取成功', 'code': '0',
                 'value':
                     {'userImageKey': 'images/2021/2/d874bec7683f4c7c99fb9b83e0c3604d.jpg',
                      'userNickname': 'leoleoleol大神大多eoleoleole阿oleoleoleoleoleoleoleoleo',
                      'userVerified': False,
                      'subscribed': True, 'userVerifyType': 2, 'userId': 6, 'type': 1, 'postId': 117}}}
    str4={'key':
              {'success': True, 'message': '获取成功', 'code': '0',
               'value': {'hasMore': True,
                         'list': [{'userId': 6,
                                   'userImageKey': 'images/2021/2/d874bec7683f4c7c99fb9b83e0c3604d.jpg',
                                   'userNickname': 'leoleoleol大神大多eoleoleole阿',
                                   'userVerified': False, 'subscribed': True, 'userVerifyType': 2, 'type': 1, 'postId': 117}]}}}

    print('postId' in str4['key']['value']['list'][0])
    # # postId = string1['value']['postId']
    # postId = str2['value']['list'][0]['postId']
    #
    # print(postId)
    # string = 'cancel=false&postId=${postId}'
    # results = re.findall(r'\$\{([^\{].+?)\}', string)
    # print(results)
    # for result in results:
    #     # value = global_variables[result]
    #     # # string = re.sub(r'\$\{' + result + '\}', str(string1[result]), string)
    #     # string =re.sub(r'\$\{'+result+'\}',value,string)
    #     # userid = string.replace(str(results), str(value[result]))
    #     print(string)
    #     #
    # string = re.sub(r'\$\{' + result + '\}', str(postId), string)
    # print(string)
