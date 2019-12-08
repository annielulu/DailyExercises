# coding:utf-8
__author__ = 'annie'

# 输入一个数字，输出对应行数的菱形图案

row = int(input('请输入生成菱形的行数:'))
while row % 2 == 0:
    row = int(input('你输入的是偶数，请输入一个奇数：'))

# 上半个行数
s = row//2+1
# 下半个行数
x = row - s
# 上半个等腰三角形
for i in range(1, s+1):
    # 打印空格
    for k in range(s - i):
        print(' ', end='')

    for j in range(i*2-1):
        print('*', end='')
    print()
# 下半个等腰三角形
for i in range(x):
    # 打印空格
    for m in range(i+1):
        print(' ', end='')

    # '*'号的数量是成倍的倒着打印
    for n in range(x*2-1, i*2, -1):
        print('*', end='')
    print()