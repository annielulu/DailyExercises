# coding:utf-8
__author__ = 'annie'

# python连接mysql、redis、mongoDB
# 1.连接mysql
import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='pydb')
print(conn)# <pymysql.connections.connection 0x0000029b3f9b6470="" at="" object="">
