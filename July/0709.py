# coding:utf-8
__author__ = 'annie'

# 1、python中断言方法举例
a = 6
assert (a > 0)
print('Success!断言成功！')
b = 2
assert (b < 0)
print('Fail！断言失败！')

# 2、python2和python3区别？列举5个
# 1）Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print 'hello,world'
#    Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hello,world')
# 2）python2 range(1,10)返回列表
#    python3中返回迭代器，节约内存
# 3）python2中使用ascii编码
#    python3中使用utf-8编码
# 4）python2中unicode表示字符串序列，str表示字节序列
#   python3中str表示字符串序列，byte表示字节序列
# 5）python2中为正常显示中文，引入coding声明
#    python3中不需要
# 6）python2中是raw_input()函数
#    python3中是input()函数




