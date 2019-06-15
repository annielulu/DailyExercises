# coding:utf-8
__author__ = 'annie'

# 如何在一个函数内部修改全局变量
# 利用global 修改全局变量
a = 1
def add():
    global a
    # a = 2
    a = a + 1
    print(a)
add()
