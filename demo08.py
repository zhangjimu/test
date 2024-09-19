# 2024/2/25 18:23
# demo08.py
# 定义函数
# 1.普通函数
def test():
    print("你好")


test()

# 2.默认参数
def a(name):
    print(name)

a("张三")


def f(a=1):
    print(a)

f()

def x(a:int):  # 定义a的传参类型
    print(a)

f("aaa")