import pandas as pd
import os
# 获取当前路径
# cwd = os.getcwd()
# 要拼接的文件夹及其完整路径，注不要包含中文
## 待读取批量csv的文件夹
read_path = '/media/hkuit164/WD20EJRX/mysql/prune_result/csv'
## 待保存的合并后的csv的文件夹
save_path = '/media/hkuit164/WD20EJRX/mysql/prune_result'
## 待保存的合并后的csv
save_name = 'Modified.csv'

# 将该文件夹下的所有文件名存入列表

csv_name_list = os.listdir(read_path)

# 读取第一个CSV文件并包含表头，用于后续的csv文件拼接
df = pd.read_csv( os.path.join(read_path,csv_name_list[0]))

# 读取第一个CSV文件并保存
df.to_csv(  save_path + '/' + save_name , encoding="utf_8",index=False)
# 循环遍历列表中各个CSV文件名，并完成文件拼接
for i in range(9):
    df = pd.read_csv( os.path.join(read_path,csv_name_list[i]) )
    df.to_csv( save_path + '/' + save_name ,encoding="utf_8",index=False, header=False, mode='a+')
