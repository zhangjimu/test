# 2023/12/3 19:41
# demo02.py
d = {
    "A": [],
    "B": []
}

while True:
    content = input("请输入内容:")
    new_content = content.split(":")  # split分隔符可自定义，格式A:111
    try:
        user, text = new_content[0], new_content[1]
    except Exception as e:
        print("请按照正确的格式输入")
        continue
    # setdefault() 是字典对象的一个方法，用于获取指定键的值，如果键不存在，则可以设置默认值并将其添加到字典中，键存在时不会改变原本键对应的值
    d.setdefault(user, [])  # 为其他用户创建默认值
    if text == "exit":
        break
    elif text == "log":
        print(d)
    else:
        d[user].append(text)
        print(text)
