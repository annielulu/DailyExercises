# coding:utf-8
__author__ = 'annie'

# 1、避免转义给字符串加哪个字母表示原始字符串？
# -- r , 表示需要原始字符串，不转义特殊字符

# 2、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
import re
str = '<div class="nam">中国</div>'
res = re.findall(r'<div class=".*">(.*?)</div>',str)  # .代表可有可无，*代表任意字符；(.*?)代表提取文本
print(res)

