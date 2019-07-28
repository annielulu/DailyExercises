# coding:utf-8
__author__ = 'annie'

# 做性能测试，需要写一个函数，批量生成一些注册使用的账号。
# 要求：1、产生的账号是以@163.com结尾
# 2、长度由用户输入，产生多少条也由用户输入
# 3、用户名不能重复
# 4、用户名必须由大写字母、小写字母、数字组成
# 5、输出结果至txt文件中，例如：testAA123@163.com；tAstsA456@163.com；sdfAs789@163.com

# 导入random模块
import random
# 导入string模块
import string

length = int(input('请输入您想要随机产生的邮箱的长度：'))
count = int(input('请输入您想要随机产生的邮箱的条数：'))

# 定义一个生成邮箱账号的函数
def email_accounts(length,count):
    # 打开一个txt文件并加写的权限
    f = open('email.txt','w')
    # 随机生成用户名
    for i in range(count):
        # 随机生成大写字母+小写字母
        result_1 = ''.join(random.sample(string.ascii_letters,length-1))
        # 随机生成数字
        result_2 = ''.join(random.sample(string.digits,1))
        # 将随机生成的大写字母+小写字母与随机生成的数字及邮箱后缀拼接起来并写入txt文件中
        f.write(result_1 + result_2 + '@163.com' + '\n')
    f.close()

# 调用
email_accounts(length,count)


