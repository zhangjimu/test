# 2024/4/1 22:29
# demo09.py
# while True:
#     content= input("请输入：")
#     print(content)


# a = 0
# # 通过bool值来决定是否继续执行
# while bool(a < 10):
#     # a<10代表当a在10以内为正程序继续运行，当a大于10为假程序不运行了
#     content = input("请输入：")
#     print(content)
#     # a = a+1代表a的值为每次执行后a的值加1
#     a = a + 1


# in用来表示在当前循环中所代表的数字是多少
# 容器行数据类型可以用来遍历，列表，字典、字符串、元组等

"""编写一个程序，提示用户输入一个字符串，然后将字符串反转并打印结果。
例如，如果用户输入"hello"，则程序应该输出"olleh"."""
# user_input = input("请输入字符串：")
# result_input = user_input[::-1]
# print(f"反转后的字符串是", {result_input})


# %是取模(取余）操作，一个数%另一个数，前面一个数-后面数乘以另一个数的差
print("I will now count my chickens")
print(25 + 30 / 6)
print(100 - 25 * 3 % 4)
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print(3 + 2 < 5 - 7)
print("what is 3+2?", 3 + 2)

# 变量的命名和使用
cars = 300
print("There are", cars, "car available")


# 字符串格式化'f'
my_name = "Zed"
my_age = 35
my_height = 74
print(f"Let is talk about {my_name}")
print(f"he is {my_height} inches tall")
print(f"he is {my_age} looks younger")

# 字符串格式化.format()
hilarious = "你好"
test = 1
print("joken_evaluation {} {}".format(hilarious, test))  # 按顺序直接匹配
print("joken_evaluation {1} {0}".format(hilarious, test))  # 按索引匹配
print(f"joken_evaluation {hilarious} {test}")  # 直接引用变量


# 浮点数四舍五入关键字 round
print(round(1.50))  # 2
print(round(1.29))  # 1
print(round(1.690))  # 2
print(round(1.9))  # 2
