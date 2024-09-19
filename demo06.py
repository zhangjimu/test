# 2023/12/17 12:47
# demo06.py
# 封装函数
# 2023/12/3 19:41
# demo02.py
# d = {
#      "A": [],
#      "B": []
#     }


def get_input():
    while True:
        content = input("请输入内容:")
        new_content = content.split(":")  # split分隔符可自定义，格式A:111
        try:
            user, text = new_content[0], new_content[1]

            return user, text
        # except Exception as e:
        except Exception:
            print("请按照正确的格式输入")
            continue


def handle(user, text, d):
    # setdefault() 是字典对象的一个方法，用于获取指定键的值，如果键不存在，则可以设置默认值并将其添加到字典中，键存在时不会改变原本键对应的值
    d.setdefault(user, [])  # 为其他用户创建默认值
    if text == "exit":
        return "exit"
    elif text == "log":
        print(d)
    else:
        d[user].append(text)  # 记录用户发言
        print(text)


def process_input():
    d = {
        "A":[],
        "B":[]
    }
    while True:
        user, text = get_input()
        ret = handle(user, text, d)
        if ret is not None:
            break


process_input()


