# coding:utf-8
__author__ = 'annie'

# 字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"

import re
a = "not 404 found 张三 99 深圳"
# 将字符串切片，分成一个个单独的字符串存放在列表中
lists = a.split(" ")
print('lists=',lists)
# 用正则过滤掉英文和数字
result = re.findall('\d+|[a-zA-Z]+',a)
print('result=',result)
# 遍历result中的值，如果lists中的值包含了result中的值，则移除lists中的这些值
for i in result:
    if i in lists:
        lists.remove(i)
# 以空格作为分隔符，返回结果
Final_output = " ".join(lists)
print('Final_output=',Final_output)

