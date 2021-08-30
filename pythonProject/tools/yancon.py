import yaml
def get_yam_data(file):
    reslist = [] #存放请求1， 响应1
    #读取文件
    fo = open(file,'r',encoding="utf-8")
    #获取数据
    res = yaml.load(fo,Loader=yaml.FullLoader)
    fo.close()
    for one in res:
        if 'data' in one:
            reslist.append((one['url'],one['data'],one['resp']))
        else:
            reslist.append((one['url'], one['json'], one['resp']))
    return reslist  #存放请求1， 响应1
if __name__ == '__main__':
    print(get_yam_data('../data/Case.yaml'))