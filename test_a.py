import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_path = '/media/hkuit164/WD20EJRX/mysql/test.xlsx'
df = pd.read_csv(csv_path)
# col = ['train_dist','train_auc']
df_corr = df[['train_dist','train_auc','val_pr']].corr()
print(df_corr)
# plt.subplots(figsize=(9, 9)) # 设置画面大小
sns.heatmap(df_corr, vmax=1,annot=True, square=True, cmap="Blues")
plt.show()


# print(df['train_AUC'].corr(df['train_PR'],method='spearman'))