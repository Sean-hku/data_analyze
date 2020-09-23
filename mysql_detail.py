# -*- coding:utf-8 -*-
import csv
import os
import numpy as np
import pandas as pd
import pymysql
from pymysql import connect
import glob

class CsvToMysql(object):
    def __init__(self, hostname, port, user, passwd, db, table_name):
        self.dbname = db
        self.conn = connect(host=hostname, port=port, user=user, passwd=passwd, db=db)
        self.cursor = self.conn.cursor()
        self.table_name = table_name

    def read_csv(self, filename):
        df = pd.read_csv(filename, keep_default_na=False, encoding='utf-8')
        self.csv2mysql(table_name=self.table_name, df=df)

    def make_table_sql(self, df):
        # 将csv中的字段类型转换成mysql中的字段类型
        columns = df.columns.tolist()
        types = df.ftypes
        make_table = []
        make_field = []
        for item in columns:
            item1 = '`' + item.replace(' ', '_').replace(':', '') + '`'
            # if item1 == '`epoch`':
            #     char = item1 + ' INT' + ' not null primary key'
            if 'int' in types[item]:
                char = item1 + ' INT'
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
# select lr,max(train_acc) from train_log group by lr;
    def csv2mysql(self, table_name, df):
        field1, field2 = self.make_table_sql(df)
        self.cursor.execute("create table if not exists {} ({})".format(table_name,field1))
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
    db = 'black'
    table_name = 'train_log'
    M = CsvToMysql(hostname=hostname, port=port, user=user, passwd=passwd, db=db,table_name=table_name)
    # csv文件目录
    a = glob.glob('/media/hkuit164/WD20EJRX/mysql/result/black/*/*.csv')
    count = 0
    for path in a:
        csv_path = os.path.join('/media/hkuit164/WD20EJRX/mysql/result/black', path)
        print(csv_path)
        count+=1
        print(count)
        M.read_csv(path)