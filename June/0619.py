# coding:utf-8
__author__ = 'annie'

# python实现列表去重的方法
# 方法一：
lists = ['1','5','6','2','4','4','7','3','7','3']
print(list(set(lists)))

# 方法二：
list2 = []
list1 = [1,2,3,4,8,4,6,8]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)