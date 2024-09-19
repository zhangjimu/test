# 2023/12/11 22:03
# demo04.py
# 函数变量的作用域
a = 1


def x():
    a = 2
    print("a in x:{}".format(a))


x()
print("a not in:{}".format(a))

# LEGB使用顺序
input = "你好"
import builtins


def f():
    global input  # 如果时全局变量可以直接声明，之后调用的都是全局变量
    input = "hello"  # 有局部作用域会调用局部作用域，没有才会调用全局作用域最后调用内置函数-作用域
    # print(input)
    # print(locals())  # 打印局部作用域，以为字典的方式
    # print(globals())  # 打印全局作用域，以为字典的方式
    # print(locals()['input'])
    print(globals()['input'])  # 以字典的形式打印
    print(builtins.input())  # 打印python中内置作用域


f()
