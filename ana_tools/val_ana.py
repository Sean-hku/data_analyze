import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_box(df,analyse_item):
    for item in analyse_item:
        fig,axes =plt.subplots(2,2,figsize=(12,12))
        df.boxplot(column='R',by=[item],ax=axes[0][0])
        df.boxplot(column='P',by=[item],ax=axes[0][1] ,)
        df.boxplot(column='mAP',by=[item],ax=axes[1][0] )
        df.boxplot(column='F1',by=[item],ax=axes[1][1] )
        plt.savefig('../val_ana/gray_warm/{}_box.png'.format(item),)

def plot_bar(df,analyse_item):
    for item in analyse_item:
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))
        df.groupby(item).P.mean().plot.bar(ax=axes[0][0])
        df.groupby(item).R.mean().plot.bar(ax=axes[0][1])
        df.groupby(item).mAP.mean().plot.bar(ax=axes[1][0])
        df.groupby(item).F1.mean().plot.bar(ax=axes[1][1])
        plt.savefig('black_ana/{}_mean.png'.format(item),)
def means_dataset(df):
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    g = lambda x: x.set_ylim(0.8, 1)
    g(axes[0][0])
    g(axes[0][1])
    g(axes[1][0])
    g(axes[1][1])
    df['P'].mean().plot.bar(ax=axes[0][0])
    df['R'].mean().plot.bar(ax=axes[0][1])
    df['mAP'].mean().plot.bar(ax=axes[1][0])
    df['F1'].mean().plot.bar(ax=axes[1][1])
    # if not os.path.exists('../test_ana'):
    #     os.makedirs('../test_ana')
    plt.savefig('../val_ana/gray_warm/mean.png')

pd.set_option('display.max_columns', 100000)
pd.set_option('display.max_rows', 1000000)
plt.style.use('ggplot')
path = '/media/hkuit164/WD20EJRX/mysql/gray_warm_result_sean.csv'
df = pd.read_csv(path)
analyse_item = ['optimize','tpye','activation','freeze','rect','multi-scale']
plot_box(df,analyse_item)
means_dataset(df)




