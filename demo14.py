# 2024/4/25 16:51
# demo14.py
import time

# 获取当前时间戳
current_timestamp = time.time()
print("当前时间戳：", current_timestamp)
# 输出：当前时间戳： 1714036873.6094098

# 获取当前时间戳-结构化表示（元组）
current_time_struct = time.localtime(current_timestamp)
print("当前时间的结构化表示:", current_time_struct)
# 输出：前时间的结构化表示: time.struct_time(tm_year=2024, tm_mon=4, tm_mday=25, tm_hour=17,
# tm_min=21, tm_sec=13, tm_wday=3, tm_yday=116, tm_isdst=0)


# 格式化达能前时间
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time_struct)
print("格式化后的当前时间：", formatted_time)
# 输出：格式化后的当前时间： 2024-04-25 17:25:02
