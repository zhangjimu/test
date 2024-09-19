# # 2024/4/3 14:24
# # demo10.py
# # while循环练习
# # while循环语句格式
# # while condition:
# #     pass
# # # condition是一个逻辑条件，可以是任何返回布尔值的表达式
#
#
# # 猜数字游戏：
# """编写一个程序，随机生成一个1到100之间的整数作为目标数字，
# # 然后提示用户猜这个数字。用户每次可以输入一个猜测的数字，
# 程序会根据用户的猜测提供相应的提示，直到用户猜对为止。
# 程序应该输出猜了几次才猜对"""
# # 导入random模块用于随机生成1-100之间的整数
# # import random
# #
# # # 生成整数
# # get_number = random.randint(1,100)
# #
# # # 初始化猜测次数
# # guesses = 0
# # while guesses <= 5:
# #     guess = int(input("请输入1到100的整数:"))
# #     guesses += 1
# #     #判断猜测数组和目标数字的关系，并给出提示
# #     if guess < get_number:
# #         print("太小了，请继续猜")
# #     elif guess > get_number:
# #         print("太大了，请继续猜")
# #     else:
# #         print(f"恭喜你猜对啦，目标数字是{get_number},共猜测了{guesses}次") #f是将变量转换为字符串
# #         break
#
#
#
#
# # """编写一个程序，随机生成一个1到100之间的整数作为目标数字，
# # # 然后提示用户猜这个数字。用户每次可以输入一个猜测的数字，
# # 限定次数只有5次，5次内猜不对程序给出提示并结束游戏"""
# # # 导入random模块用于随机生成1-100之间的整数
# # import random
# #
# # # 生成整数
# # get_number = random.randint(1,100)
# #
# # # 初始化猜测次数
# # guesses = 0
# # while guesses < 5:
# #     guess = int(input("请输入1到100的整数:"))
# #     guesses += 1
# #     #判断猜测数组和目标数字的关系，并给出提示
# #     if guess < get_number:
# #         print("太小了，请继续猜")
# #     elif guess > get_number:
# #         print("太大了，请继续猜")
# #     else:
# #      print(f"恭喜你猜对啦，目标数字是{get_number},共猜测了{guesses}次") #f是将变量转换为字符串
# #      break
# #
# #
# # if guesses == 5 and guess != get_number:
# #     print(f"很遗憾没有次数了，目标数字是{get_number}")
#
#
#
#
# # 获取用户输入的正整数
# num = int(input("请输入一个正整数："))
#
# # 初始化数字之和为0
# sum_of_digits = 0
#
# # 计算各个数字之和
# while num > 0:
#     # 获取最后一位数字
#     digit = num % 10
#     # 将最后一位数字加到数字之和中
#     sum_of_digits += digit
#     # 去掉最后一位数字
#     num //= 10
#
# # 打印结果
# print("输入正整数各个数字之和为:", sum_of_digits)






# 以只读模式打开文件,读取整个文件
with open("test.txt","r") as file:
    content = file.read()
    print(content)


# 逐行读取readline()
with open("test01.txt","r") as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()


# 读取前几个字符串readline(XX)
with open("test01.txt","r") as file:
    # 读取前3个字符
    print(file.read(3))


# 读取所有行readlines()
with open("test01.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)


# 以写入模式打开文件,会覆盖原有的文件内容，文件不存在时会创建文件
# 方法一
with open("test01.txt","w") as file:
    # 全部写入
    print(file.write("hello,my name is ZD"))

# 方法二
with open("test01.txt","w") as file:
    content = file.write("hhhhhh")
    print(content)


# 写入多行writelines()--按行写入
line = ["hello\n","你好\n","china\n"]
with open("test01.txt","w") as file:
    print(file.writelines(line))


# 文件追加a,
with open("test.txt","a") as file:
    print(file.write("this is a example\n"))
# 追行追加a,writelines()
l = ["name\n","hello\n"]
with open("test.txt","a") as file:
    print(file.writelines(l))






import os

file_path = "test.txt"
absolute_path = os.path.abspath(file_path)
print("文件的绝对路径:", absolute_path)