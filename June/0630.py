# coding:utf-8
__author__ = 'annie'

# 求列表中第二大元素

# 方法一：直接从小到大排序，输出倒数第二个数
lists = [3,6,8,10,5,7,11,22,56,88,45,99]
sort_lists = sorted(lists)
print('排序后的列表为：',sort_lists)
print('第二大元素为：',sort_lists[-2])

# 方法二：设置标志位，遍历列表找出第二大的数
def second(lists):
    max = 0
    s = {}
    for i in range(len(lists)):
        flag = 0
        for j in range(len(lists)):
            if lists[i] >= lists[j] and i != j :
                flag = flag + 1
        s[i] = flag
        if flag > max:
            max = flag
    print('s:\n',s)
    for i in s:
        if s[i] == max - 1:
            break
    print('第二大元素为：',lists[i])


second([3,6,8,10,5,7,11,22,56,88,45,99])


