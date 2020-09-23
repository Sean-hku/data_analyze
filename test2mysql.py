# -*- coding:utf-8 -*-
import csv
import os
import numpy as np
import pandas as pd
import pymysql
from pymysql import connect
import re

class CsvToMysql(object):
    def __init__(self, hostname, port, user, passwd, db,table_name):
        self.dbname = db
        self.conn = connect(host=hostname, port=port, user=user, passwd=passwd, db=db)
        self.cursor = self.conn.cursor()
        self.table_name = table_name

    def read_csv(self, filename):
        df = pd.read_csv(filename, keep_default_na=False, encoding='utf-8')
        self.csv2mysql( table_name=self.table_name, df=df)

    # if the tables exist when create a new table
    def table_exists(self):
        sql = "show tables;"
        self.cursor.execute(sql)
        tables = [self.cursor.fetchall()]
        table_list = re.findall('(\'.*?\')', str(tables))
        table_list = [re.sub("'", '', each) for each in table_list]
        if self.table_name in table_list:
            return 1  # 存在返回1
        else:
            return 0

    def make_table_sql(self, df):
        # 将csv中的字段类型转换成mysql中的字段类型
        columns = df.columns.tolist()
        types = df.ftypes
        make_table = []
        make_field = []
        for item in columns:
            item1 = '`' + item.replace(' ', '_').replace(':', '') + '`'
            # primary key setting
            if item1 == '`ID`':
                char = item1 + ' INT'
            elif 'int' in types[item]:
                char = item1 + ' FLOAT'
            elif 'float' in types[item]:
                char = item1 + ' FLOAT'
            elif 'object' in types[item]:
                char = item1 + ' VARCHAR(255)'
            elif 'datetime' in types[item]:
                char = item1 + ' DATETIME'
            else:
                char = item1 + ' VARCHAR(255)'
            make_table.append(char)
            make_field.append(item1)
        return ','.join(make_table), ','.join(make_field)

    def csv2mysql(self, table_name, df):
        field1, field2 = self.make_table_sql(df)
        print("create table {} ( {})".format(table_name, field1))
        # self.cursor.execute('drop table if exists {}'.format(table_name))
        if self.table_exists():
            print('Warming, table exists!!')
            os._exit(1)
        self.cursor.execute("create table {} ({})".format(table_name,field1))
        values = df.values.tolist()
        s = ','.join(['%s' for _ in range(len(df.columns))])
        try:
            print(len(values[0]), len(s.split(',')))
            self.cursor.executemany('insert into {}({}) values ({})'.format(table_name, field2, s), values)
        except Exception as e:
            print(e.message)
        finally:
            self.conn.commit()


if __name__ == "__main__":
    hostname = 'localhost'
    port = 3306
    user = 'root'
    passwd = '123456'
    db = 'ceiling'
    table_name = 'test_A'
    csv_path = '/media/hkuit164/WD20EJRX/mysql/test_result/ceiling_test_result.csv'
    M = CsvToMysql(hostname=hostname, port=port, user=user, passwd=passwd, db=db,table_name=table_name)
    # csv文件目录
    M.read_csv(csv_path)