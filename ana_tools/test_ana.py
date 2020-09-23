import pandas as pd
import matplotlib.pyplot as plt
import os
def test_boxplot(df,analyse_item,test_item):
    for item in analyse_item:
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))
        # g = lambda x: x.set_ylim(0.7, 1)
        # g(axes[0][0])
        # g(axes[0][1])
        # g(axes[1][0])
        # g(axes[1][1])
        df.boxplot(column='R',by=[item],ax=axes[0][0])
        df.boxplot(column='P',by=[item],ax=axes[0][1] ,)
        df.boxplot(column='mAP',by=[item],ax=axes[1][0] )
        df.boxplot(column='F1',by=[item],ax=axes[1][1] )
        plt.show()
        if not os.path.exists('../test_ana/{}'.format(test_item)):
            os.makedirs('../test_ana/{}'.format(test_item))
        # plt.savefig('../test_ana/{}/{}_box.png'.format(test_item,item))
def means_dataset(df):
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    g = lambda x: x.set_ylim(0.7, 1)
    g(axes[0][0])
    g(axes[0][1])
    g(axes[1][0])
    g(axes[1][1])
    df.groupby('test_data').P.mean().plot.bar(ax=axes[0][0])
    df.groupby('test_data').R.mean().plot.bar(ax=axes[0][1])
    df.groupby('test_data').mAP.mean().plot.bar(ax=axes[1][0])
    df.groupby('test_data').F1.mean().plot.bar(ax=axes[1][1])
    if not os.path.exists('../test_ana'):
        os.makedirs('../test_ana')
    # plt.show()
    plt.savefig('../test_ana/mean1.png')
    # plt.show()

pd.set_option('display.max_columns', 100000)
pd.set_option('display.max_rows', 1000000)
plt.style.use('ggplot')
path = '/media/hkuit164/WD20EJRX/yolov3-channel-and-layer-pruning/gray_test_result.csv'
df = pd.read_csv(path)
means_dataset(df)
# test_item = ['far.data','mul.data','all.data','single_front.data','single_side.data']
# for items in test_item:
#     df_far = df[df['test_data']== items]
#     analyse_item = ['optimize','tpye','activation','freeze','rect',]
#     test_boxplot(df_far,analyse_item,items)