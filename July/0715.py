# coding:utf-8
__author__ = 'annie'

# s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
m = set(s) # 去重
t = sorted(m)  # 从小到大排序
item = ''.join(t)  # 将列表中的每一个元素拼接成一个字符串
print(m)
print(t)
print('输出结果为：',item)

