# coding:utf-8
__author__ = 'annie'

# 有一个已经排好序的数组，现输入一个数，要求按原来的规律将它插入数组中
a = [3,5,8,11,25,36,48,50,88,90]
b = []
print('初始数组为：\n',a)
n = int(input('请输入要插入的数字：'))
def insertArray():
    for i in a:
        if n < i and not b.__contains__(n):
            b.append(n)
        elif n == i:
            b.append(n)
            b.append(i)
        else:
            b.append(i)
    if b.__contains__(n):
        pass
    else:
        b.append(n)
    print('插入输入的数字后的数组为：\n',b)

insertArray()



