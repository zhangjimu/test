# 2024/4/21 21:58
# demo13.py
# 时间模块
# UTC时间
# 起步时间1970年1月1日 00:00:00
import time
from time import *

print(time())   # 从时间起点到现在时间的秒数

# sleep(3)  # 休眠三秒后再执行（最少休眠3秒）

print(time())

print(gmtime(time()))   # 获取当前年月日时间这里获取的是utc时间
print(localtime())      # 获取本地时间，北京时间=utc时间+8

_time = localtime()
print("{}年{}月{}日".format(_time.tm_year, _time.tm_mon, _time.tm_mday))   # 获取本地时间

# 将时间格式为字符串 默认获取本地的时间strftime
print(strftime("%Y-%m-%d %H:%M:%S"))   #
print(strftime("%Y-%m_%d %H:%M:%S", gmtime(1))) # 使用utc时间再起步时间加1秒 1970-01_01 00:00:01


# 将字符串转换为时间格式strptime
print(strptime("2023-09-03 22:02:10", "%Y-%m-%d %H:%M:%S"))


current_timestamp = time.time()
print(("当前时间戳：", current_timestamp))

