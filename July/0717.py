# coding:utf-8
__author__ = 'annie'

# 字典根据键从小到大排序dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
dicts={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
lists = sorted(dicts.items(),key=lambda i:i[0],reverse = False)
print(lists)

# results = dict(lists)
# print(results)
