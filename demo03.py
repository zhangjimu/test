# 2023/12/10 15:40
# demo03.py
# 函数相关
# 1.函数定义和调用
def name():  # 定义函数def +可读性函数名+():
    print("请输入您的姓名")


name()  # 调用函数函数名+()


# 普通参数
def hello(name):  # 定义一个普通参数name,调用时必须给name传参
    print("你好", name)


hello("张朵")


# 默认参数
# 无默认参数的普通参数不能放在有默认参数的普通参数后面（只能放在默认参数之前且调用时必须传参），否则会报错
def hello(hi, name="张三"):
    print(hi, name)


hello("你好")
hello("你好", "张几木")


def test(hi, name="我是test"):
    print(hi, name)


test("hello")



def f(l=[]):
    # print(l.append(1))   为什么不能用这种方式写
    l.append(1)
    print(l)


f()
f()


# 不定长参数
def s(*args, **kwargs):  # 单*标识用来传递位置参数，双**表示用来传递关键字参数如：字典
    print(args)  # 元组，存储位置参数
    print(kwargs)  # 字典，存储关键字参数
    print("-" * 20)


s(1, 2, 3)  # 只传递位置参数
s(name="张朵")  # 只传递字典参数
s()  # 不传递参数


# 函数的返回值，每个函数一定有有一个返回值
def add(a, b):
    c = a + b
    print("a+b的和是:", c)


add(1, 11)


# print(res)  默认返回值为None


# 将c的值和100相加
# 方法1，改变函数的默认返回值，将返回值c的值和100相加改变函数的返回值可以使用return
def add(a, b):
    c = a + b
    print("a+b的和是:", c)
    return c  # 返回值为c的值


res = add(1, 11)
# print(res)  查看函数的返回值
add(res, 100)  # 112


# 方法2，用元组的方式打印a,b,c的值，将c的值与100相加
def add(x, y):
    d = x + y
    print("x+y的值为：", d)
    return x, y, d


x, y, d = add(1, 2)  # 用赋值的方式将1，2，3的值赋值给x, y ,d
add(d, 100)  # 将d的值和100相加
