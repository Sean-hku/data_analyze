import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100000)
pd.set_option('display.max_rows', 1000000)
plt.style.use('ggplot')
path = '/media/hkuit164/WD20EJRX/mysql/prune_result/Modified.csv'
df = pd.read_csv(path)
df_fine = df[df['model'].str.contains('finetune')]
print(df_fine)
# print(df)
# print(df.info())
df = df.dropna()

fig, axes = plt.subplots(2, 2, figsize=(20, 20))
g = lambda x: x.set_xlim(0.8, 1)
# g(axes[0][0])
# g(axes[0][1])
# g(axes[1][0])
g(axes[1][1])
df.groupby('model').para.mean().plot.barh(ax=axes[0][0])
df.groupby('model').mAP.mean().plot.barh(ax=axes[0][1])
df.groupby('model').time.mean().plot.barh(ax=axes[1][0])
df_fine.groupby('model').mAP.mean().plot.barh(ax=axes[1][1])
plt.xticks(rotation=15,fontsize=6)
plt.show()
# df_dup = df.drop_duplicates(subset='para')
