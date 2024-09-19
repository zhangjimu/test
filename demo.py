# # 2023/7/2 17:30
# # demo.py
# print('hello')
#
# # 给定半径求圆的面积和周长，圆周率3.14
# r = int(input("请输入圆的半径"))
# print("圆的面积为:",3.14*r*r)
# print("圆的周长为:",3.14*2*r)
# # 2.输入2个数比较大小后从小到大升序打印
# a = input("请输入数字:")
# b = input("请输入数字:")
# if a > b:
#     print(a,b)
# else:
#     print(b,a)
# #3.一次输入若干个整数，打印出最大值，若输入为空则退出程序
# #4.给定一个不超过5位的正整数（不转换为字符串），判断该数的位数依次打印出万位千位百位十位各位的数字
# a = input("请输入一个不超过5位数的正整数:")
# if len(a) > 5:
#     print("长度大于5位数")
# else:
#     print("长度在5位内")
# # 5.给定一个不超过5位数的正整数判断该位数是几位数依次从万位打印到个位的数字
# # 6.输入n个数，求每次输入后的算术平均数
# a = int(input("请输入一个数"))
# b = int(input("请输入另一个数"))
# c = a+b//2
# print("平均数为:",c)
# # 7.打印一个边长为n的正方形
# n = int(input("请输入正方形的边长"))
# i = 1
# while i<= n:
#     if i --1 or i == n:
#         print("*"*n)
#     else:
#         print("*"+"*(n-2)"+"*")
#     i = i+1
# # 8.求100内所有奇数的和
# sum = 0
# for i in range(1,100,2):
#     sum += i
# print(sum)
# for循环
a = 100
b = 200
print(a)
print(b)
if a > 100:
    print("通过")
if a:           #a=100
    print(a,"~~~")
if a -100:      #a-100=100
    print("100")
else:
    print("a小于100")

# 嵌套
a = 5
if a == 0:
    print("zero")
else:
    if a > 0:
        print("通过")
    else:    #隐含条件：a<0或a=0
        print("不通过")
# while循环：死循环或不确定循环的次数
# while True:   #条件满足进入条件直到条件不满足
#     print("1")

a = 10
while a:
    print(a)  #输出1-10
    a -= 1

a = -10
while a:
    print(a)
    a += 1

# 遍历:容器中所有的元素不重复的取一遍，只读一遍容器中的数据不会减少
for i in [1,2,3]:
    print(i)

range(10)  #rang(0,10) 内建函数，直接返回一个range对象并不是直接立即返回数据
# 惰性对象，必须使用一些方法去拿数据，不拿不会返回，需配合其他函数一起使用如for
for i in range(10): #for语句会一次次取出range中的数，直到取完
    print(i)  # 0~9
# 计算10以内的奇数
for i in range(10):
    if i % 2 == 1:  #取余
        print(i)
#计算2**0到2**10
for i in range(11):
    print(i,2**1)