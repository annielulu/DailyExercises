# coding:utf-8
__author__ = 'annie'

# 利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"

# 导入collections库、Counter方法
from collections import Counter
a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# 统计次数
result = Counter(a)
print(result)
