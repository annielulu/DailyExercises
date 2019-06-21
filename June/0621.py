# coding:utf-8
__author__ = 'annie'

# fun(*args,**kwargs)中的*args,**kwargs什么意思?
# *args:*args表示任何多个无名参数，它是一个tuple
# **kwargs:**kwargs表示关键字参数，它是一个dict
def foo(*args,**kwargs):
    print('args=',args)
    print('kwargs=',kwargs)
    print('------------------')
if __name__ == '__main__':
    foo(1,2,3)
    foo(a=1,b=2,c=3)
    foo(1,2,3,a=1,b=2,c=3)
    foo(1,'b','c',a=1,b='b',c='c')