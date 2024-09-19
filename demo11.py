# 2024/4/21 11:20
# demo11.py
# 异常处理相关

# 例一
try:
    # 输入可能出现异常的代码
    result = 10 / "1"
except ZeroDivisionError:
    # 处理特定类型的异常
    print("除数不能为零")
except Exception as e:
    print("发生异常:", e)

# 捕获特定异常并抛出新异常：
try:
    age = int(input("请输入年龄:"))
    if age < 0:
        raise "年龄不能小于0"
except Exception as ve:
    print("输入错误：", ve)
    # 手动抛出异常
    raise RuntimeError("年龄输入错误!") from ve

# 处理异常同时保留原始异常信息
try:
    result = 10 / 1
except ZeroDivisionError:
    raise RuntimeError("除数不能为0") from None


# python中定义函数f，可以接受任意个关键字参数，并且不接受位置参数
def f(**kwargs):
    for key, value in kwargs.items():
        print(f"关键字参数{key}的值为：{value}")


f(a=1, b="你好")



