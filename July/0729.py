# coding:utf-8
__author__ = 'annie'

# 列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [i for i in a if i%2 == 1]
print(new_list)