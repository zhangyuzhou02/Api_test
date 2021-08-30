
from common.run import global_variables
import re

def rest_data(string):
    if string != None:
        results = re.findall(r'\$\{([^\{].+?)\}', string)
        if results != None:
            for result in results:
                # print(res)
                # print(type(res))
                # if result =='userId' or result =='postId':
                # if 'result' in global_variables.keys():
                # if result in global_variables['key']['value']['list'][0]:
                if (result in global_variables['key']['value']['list'][0]) == True:
                    value = global_variables['key']['value']['list'][0][result]
                    data = re.sub(r'\$\{' + result + '\}', str(value), string)
                else:
                    value = global_variables['key']['value'][result]
                    data = re.sub(r'\$\{' + result + '\}', str(value), string)
    else:
        data = string
    return data