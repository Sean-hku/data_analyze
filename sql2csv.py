# # -*- coding: utf-8 -*-
import pymysql
import pandas as pd

#连接配置信息
config = {
          'host':'localhost',
          'port':3306,#MySQL默认端口
          'user':'root',#mysql默认用户名
          'password':'123456',
          'db':'black',#数据库
          'charset':'utf8',
          'cursorclass':pymysql.cursors.DictCursor,
          }

# 创建连接
con= pymysql.connect(**config)
# 执行sql语句
try:
    with con.cursor() as cursor:
        sql="select * from test_A"
        cursor.execute(sql)
        result=cursor.fetchall()
finally:
    con.close()
df=pd.DataFrame(result)#转换成DataFrame格式
print(df.info())