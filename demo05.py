# 2023/12/17 11:40
# demo05.py
# # 匿名函数
# def f(add):
#     print("收到的函数{}".format(add))  # format用来格式化字符串，可以用来插入变量值、格式化数字、设置对其方式等在这里是插入变量的值add填充
#     print("调用的函数{}".format(add(1, 2)))  # {}充当占位符
#
#
# f(lambda a, b: a + b)
#
# print(help())


a = 1
type(a)
isinstance(a,int)
dir(a)
id(a)
help(a)


def main():
    filename = input("请输入文件名称")

    try:
        with open (filename, "x") as f:
            print("创建成功")
            pass
    except Exception as e:
        print("创建失败，文件已存在:{}".format(e))

main()



