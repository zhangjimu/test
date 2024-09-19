# 2023/8/6 16:28
l2 = list() # 空列表
l3 = [1,2,3] # 列表
l4 = [1,2,True,None,[3,4],"abc",2.14] # 列表中元素可以是数字、字符串、对象、列表等
l5 = list() # 括号中写可迭代对象(可以被遍历的对象)
# 例如，range(),返回一个可迭代对象for
# 函数调用，在函数的后面加上括号，括号中写上对应的值---print()
list() #列表中必须放一个可迭代对象，不能是单独的数字
# 例如：list(range(5))      list([1, "abc", 100])等。
l6 = [10,20,30,20,20,50]
print(l6.index(10))
print(l6.count(30))
print(l6[0])  #利用索引查找，O(1),与规模无关，统计出指定值出现的次数
# index和count性能很差一般不推荐使用，一般推荐使用索引
print(len(l6))  #求列表的长度
# 修改--利用索引进行修改
l6[1] = 1000
print(l6)
l6.append(90)   #append内部尾部追加
print(l6)
l6.insert(3,90)  #通过索引进行插入insert(index,value)
print(l6)
input("请输入您的姓名:")

