# coding:utf-8
__author__ = 'annie'

# 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
# map(）函数：
# 1.map()它接收一个函数 f 和一个可迭代对象(这里理解成 list)，
# 2.并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回

# 第一步：输入给定列表的平方
lists = [1,2,3,4,5]
def f(x):
    return x*x
print(list(map(f,lists)))
# 第二步：使用列表推导式提取出大于10的数
num = map(f,lists)
num = [i for i in num if i > 10]
print(num)



