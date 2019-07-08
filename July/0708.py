# coding:utf-8
__author__ = 'annie'


# python中生成随机整数、随机小数、0--1之间小数方法

# 1.生成随机整数：random.randint(a,b) -- 生成（a - b）区间内的随机整数
import random
RandomInt = random.randint(1,100)
print('随机整数为：',RandomInt)

# 2.生成随机小数：
# 方法一：使用numpy库，np.random.randn(n) -- 生成n个随机小数
import numpy as np
RandomF = np.random.randn(3)
print('随机小数为：',RandomF)

# 方法二：1.生成随机数，浮点类型 2.保留2位小数：round(数值，精度)
RandomF = random.uniform(1,10)
print('随机小数为：',round(RandomF,2))

# 3.生成0-1之间小数：random.random(),括号中不传参
RandomS = random.random()
print('0-1之间小数为：',round(RandomS,2))




