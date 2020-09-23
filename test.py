import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 100000)
pd.set_option('display.max_rows', 1000000)
# pd.set_option('display.width', 5000)

# def modify_id(path):
plt.style.use('ggplot')
path = 'ceiling-mobile_13kps_result_server2.csv'
df = pd.read_csv(path)
# print(df.corr())#计算所有的相关系数
#pearson 连续型变量 spearman允许是可排序的分类变量
print(df['train_acc'].corr(df['val_acc'],method='spearman'))#计算某个变量的相关系数
# print(df.iloc[:,9:14].mean())
# df.iloc[:,9:14].count().plot(kind= 'bar')#多变量分析
plt.figure()
df.plot(kind='scatter',x='train_acc',y='val_acc')#散点图
# plt.show()
plt.figure()
# df.plot(kind='bar',x='optimizer',y='val_acc')
# df['val_acc'].groupby(df['optimizer']).mean().plot.bar()
# df.groupby(['optimizer','freeze_bn']).val_acc.mean().plot.bar()#等价于上
df['training_time'].groupby(df['optimizer']).mean().plot.bar()
plt.legend()

# df['train_acc'].hist(bins=10)
plt.show()
# print(df.describe())