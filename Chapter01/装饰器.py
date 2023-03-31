# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 上午10:01
# @FileName: 装饰器.py
# @Software: PyCharm

from functools import wraps
def Printsumcharswithparameter(parameter):
    def Printsumchars(function):
        @wraps(function) #用于显示原函数的所有特性。
        def inner(*args, **kwargs):
            print(parameter)
            print("现在开始调用已有函数!")
            res = function(*args, **kwargs)  # 执行函数,我们自己已经写的函数。
            print("该函数执行完毕，已经返回相关的值!\n")
            return res

        return inner
    return Printsumchars


@Printsumcharswithparameter(parameter="task1")
def SumOfNumber(a, b):
    sum = a + b
    print(f"这两个数字的和是：{sum}")
    return sum


@Printsumcharswithparameter(parameter="task2")
def productOfNumber(a, b):
    product = a * b
    print(f"这两数字的积是：{product}")
    return product


# 调用
sum_this_two_number = SumOfNumber(a=1, b=2)
product_this_two_number = productOfNumber(1, 2)

