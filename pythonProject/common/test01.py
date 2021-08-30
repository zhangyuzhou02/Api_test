
def get_targe_value(request_body,result,data):
    # 循环字典，获取键、值
    for key, values in request_body.items():
        # 判断值的type类型，如果是list,调用get_list() 函数，
        if type(values) == list:
            get_list(values)
        # 如果是字典，调用自身
        elif type(values) == dict:
            get_targe_value(values)
        # 如果值不是list且是需要被替换的，就替换掉
        elif type(values) != list and key ==result:
                request_body[key] = data
        else:
            pass

def get_list(values):
    rustle = values[0]
    if type(rustle) == list:
        get_list(values)
    else:
        get_targe_value(rustle)


if __name__ == '__main__':
    # 实例
    request_body = {"name": "小明",
                    "orderon": "0001",
                    "lists":
                    [
                        {
                        "ordername": "需要被替换的值",
                        "age": "85",
                        "prangede":
                        [
                            {
                            "sku_name": "sku_1",
                            "sku_id": "需要被替换的值",
                            "sku_x": "嘻哈"
                            }
                        ]
                    }
                ]
            }

    get_targe_value(request_body)
    print(request_body)