import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# def modify_id(path):
pd.set_option('display.max_columns', 100000)
pd.set_option('display.max_rows', 1000000)

plt.style.use('ggplot')
path = 'rgb/rgb_result_sean.csv'
df = pd.read_csv(path)
print(df.info())
print(len(df['ID'].unique()))


# df_dup = df.drop_duplicates(subset='id')
# print(df_dup.groupby(['optimizer','freeze']).train_acc.agg(['max','mean']).sort_values(by='mean').plot.bar())# group by optimizer
# print(df_dup.info())
# print(df_dup.optimizer.value_counts())
# print(df_dup.describe())
# df_dup = df_dup.freeze_bn.astype(object)
# df_dup['freeze_bn'].astype('object')
# df_dup_fr = df_dup[np.bitwise_not(df_dup['freeze_bn'])]# choose False
# df_dup.groupby('optimizer').()
# print(df_dup)

# df.boxplot(column='mAP',by=['tpye'])#画箱线图
'''
fig,axes =plt.subplots(2,2,figsize=(12,12))
df.boxplot(column='R',by=['optimize'],ax=axes[0][0])
df.boxplot(column='P',by=['optimize'],ax=axes[0][1] )
df.boxplot(column='mAP',by=['optimize'],ax=axes[1][0] )
df.boxplot(column='F1',by=['optimize'],ax=axes[1][1] )
'''
# df.boxplot(column='train_time',by=['activation'])
# ax = df_dup.boxplot(column='train_acc',by=['optimizer'])
# df_dup.plot(kind='scatter',x='freeze',y='train_acc')#散点图 观察两个一维数据的关系
# df_dup.plot(kind= 'bar')
# for lable in ax.get
# df_dup.final_epoc.hist(bins=15)
# df_dup.train_acc.hist(bins=10)#acc 的分布
df.groupby('tpye').train_time.mean().plot.bar()
# df_dup.plot.scatter(x='id',y='train_acc')
# df_dup['train_acc'].plot(kind='kde')#分布的概率密度 类似直方图

# plt.savefig('activation_time.png',)
plt.show()
