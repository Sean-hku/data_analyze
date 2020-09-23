import os
import glob
import pandas as pd
def addcsv(path,table_name,model_name):
    df = pd.read_csv(path)
    # print(df)
    df.insert(df.shape[1], 'model_num', model_name)
    df.insert(df.shape[1], 'table_num', table_name)
    # df.drop(['Unnamed_0'], axis=1, inplace=True)
    # print(df)
    df.to_csv(path,index=0)

if __name__ == '__main__':
    table_name = 'A_warm'
    a= glob.glob('/media/hkuit164/WD20EJRX/mysql/result/gray_warm/*/*.csv')
    for path in a:
        csv_path = os.path.join('/media/hkuit164/WD20EJRX/mysql/result/gray_warm',path )
        model_name = csv_path.split('/')[-2]
        addcsv(csv_path,table_name,model_name)
        print(csv_path)
        print(model_name)