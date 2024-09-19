# 2023/10/29 12:15
# test.py
# for i in range(11):
#     print(i,2**i)
#
# #倒着打印10以内的奇数
# # 方法一：
# for i in range(9,0,-1):
#     if i % 2 ==1:
#         print(i)
# # 方法二：推荐使用效率更高
# for i in range(9,0,-2):
#     print(i)

# 倒着打印10以内的偶数
# # t推荐使用第一种
# for i in range(8,-1,-2):
#     print(i)
#
# for i in range(8,-1,-1):
#     if i % 2 ==0:
#         print(i)
# 使用continue打印10以内的偶数
# for i in range(10):
#     if i % 2 ==1:  continue  #i%2等于1的时候跳过，输出i%2不等于1的数--偶数
#     print(i)
# 计算1000以内能被7整除的前20个数
# count = 0
# for i in range(7,1000,7):
#     count += 1
#     print(count,i)
#     if count >=20:
#         break

# 100以内所有奇数的和
# fangfayi
sum = 0
for i in range(1,100,2):
    sum = sum + i
print(sum)

sum = 0
for i in range(0,100):
    if i % 2 ==1:
        sum += i
print(sum)
# else子句，正常循环else子句能执行，包括可迭代对象中是0-range(0);被break打破后不执行else子句
for i in range(10):
    continue
else:
    print("ok")

for i in range(0):
    continue
else:
    print("ok")

for i in range(10):
    if i ==10:
        break
else:
    print("ok")



def hello(name):  # 定义一个普通参数name,调用时必须给name传参
    print("你好")


hello("张朵")


# 反转字符串
s = "we will rick you"
s1 = s[::-1]
print(s1)



# 假设列表l = [1,2,3,[4.5.6]],请编写代码打印出列表的4
l = [1,2,3,[4,5,6]]
# 用切片的方式取值
print(l[3][0])

# 字典d = {"a":1,"b":2},取出字典所有的key
d = {"a":1,"b":2}
# 在循环中使用可迭代试图获取key
for key in d.keys():
    print(key)
# 转换为列表输出
keys_list = list(d.keys())
print(keys_list)