# coding:utf-8
__author__ = 'annie'

# 字典如何删除键和合并两个字典

# 定义一个字典a
a = {'Lily':70,'Lucy':80,'Jack':90}
print(a)

# 删除字典中的键Lily
del a['Lily']
print(a)

# 合并字典
# 定义一个字典b
b = {'Peter':98}

# 合并字典a和字典b
a.update(b)
print(a)
