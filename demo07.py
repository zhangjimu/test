# # 2024/1/28 16:12
# # demo07.py
# # 代码调试debug
# a = 1
# print(a)
#
# # breakpoint()  # 断点
# aaa = 222
#
#
# def a(i):
#     print(1)
#     print(3)
#     print(4)
#
#
# a(aaa)
#
# # l = {1, 2, 3, 4}
# def f():
#     a = 1
#     b = 2
#     c = a + b
#
#     print(c)
#
#
# f()

l = ["1", (), [], {}, set()]
for i in l:
    print(len(l))


# 面向对象特性-继承中的复制代码
class A:
    i = 1
    ii = 11
    iii = 111


class B(A):
    # B继承A的所有
    i = 3


print(B.i)  # B中有数据是会优先使用B中自己的数据  输出：3
print(B.ii)  # 输出：11
print(B.iii)  # 输出：111
