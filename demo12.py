# 2024/4/21 16:41
# demo12.py
# 导入csv文件
import csv

# 1.用列表的形式创建数据
l = [
    ["姓名", "年龄", "性别"],
    ["张三", 15, "女"],
    ["李四", 20, "男"],
    ["王五", 25, "女"],
]

with open("test02.txt", "w", encoding="utf-8-sig", newline='') as csvfile:
    # newline=''在csv文件中不对列表文件进行分隔,指定在写入文件时不要自动插入换行符。
    writer = csv.writer(csvfile)   # 创建一个 CSV 文件写入器对象 writer，它可以将数据写入到指定的 CSV 文件中。
    for _ in l:  # 循环遍历列表 l 中的每一行数据。
        writer.writerow(_)  # 对于列表中的每一行数据，调用 writer.writerow() 方法将其写入到 CSV 文件中。_ 表示当前遍历到的子列表，即一行数据


# 2.以列表的形式读取文件
with open("test02.csv", "r", encoding="utf-8-sig", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for i in reader:
        print(i)


# 字典的形式创建文件
d = [
    {"姓名": "张三", "性别": "男", "年龄": 21},
    {"姓名": "李四", "性别": "女", "年龄": 31},
    {"姓名": "王五", "性别": "女", "年龄": 11},
]

with open("dict01.csv", "w", encoding="utf-8-sig", newline='') as csvfile:
    # writer = csv.DictWriter(csvfile, fieldnames=["姓名", "年龄", "性别"])
    writer = csv.DictWriter(csvfile, fieldnames=d[0].keys())   # 获取字典第一行的所有key
    # 字典类型数据需要先提取表头
    writer.writeheader()
    # 写入数据
    for x in d:
        writer.writerow(x)


# delimiter = ''以什么为分隔符，python3.5字典是无需的所有读取出来的文件可能顺序不一样
# 4.字典的形式读取文件
with open("dict01.csv", "r", encoding="utf-8-sig", newline='') as csvfile:
    readers = csv.DictReader(csvfile)

    for d in readers:
        print(d)
