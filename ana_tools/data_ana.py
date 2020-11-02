import pandas as pd
import matplotlib.pyplot as plt
import os
class data_analyze:
    def __init__(self,path,ana_item,target_item,save_img=True):
        pd.set_option('display.max_columns', 100000)
        pd.set_option('display.max_rows', 1000000)
        plt.style.use('ggplot')
        self.path = path
        self.df = pd.read_csv(self.path)
        self.ana_item = ana_item
        self.save_img = save_img
        self.target_item = target_item
    def boxplot(self, analyse_item):
        df =self.df
        for item in analyse_item:

            fig, axes = plt.subplots(2, 2, figsize=(12, 12))
            # for target in self.target_item:
            #     df.boxplot(column=target,by=[item],ax=axes[0][0])
            df.boxplot(column='train_acc', by=[item], ax=axes[0][0])
            df.boxplot(column='train_loss', by=[item], ax=axes[0][1])
            df.boxplot(column='val_acc', by=[item], ax=axes[1][0])
            df.boxplot(column='val_loss', by=[item], ax=axes[1][1])

            # if self.save_img:
            #     plt.savefig('../val_ana/coco/{}_box.png'.format(item))
        plt.show()

    def val_means_dataset(self):
        df = self.df
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
        if self.save_img:
            plt.savefig('../val_ana/gray_warm/mean.png')

    def test_means_dataset(self,test_item):
        df = self.df
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))
        g = lambda x: x.set_ylim(0.8, 1)
        g(axes[0][0])
        g(axes[0][1])
        g(axes[1][0])
        g(axes[1][1])
        df.groupby('test_data').P.mean().plot.bar(ax=axes[0][0])
        df.groupby('test_data').R.mean().plot.bar(ax=axes[0][1])
        df.groupby('test_data').mAP.mean().plot.bar(ax=axes[1][0])
        df.groupby('test_data').F1.mean().plot.bar(ax=axes[1][1])
        # plt.show()
        if not os.path.exists('../test_ana'):
            os.makedirs('../test_ana')
        if self.save_img:
            plt.savefig('../test_ana/mean.png')
        plt.savefig('../111.png')


class data_analyze_two:
    def __init__(self,path1,path2,ana_item,save_img=True):
        pd.set_option('display.max_columns', 100000)
        pd.set_option('display.max_rows', 1000000)
        plt.style.use('ggplot')
        self.path1 = path1
        self.path2 = path2
        self.df1 = pd.read_csv(path1)
        self.df2 = pd.read_csv(path2)
        self.df_m = pd.merge(self.df1, self.df2, on='ID', suffixes=('_path1', '_path2'))
        self.ana_item = ana_item
        self.save_img = save_img

    def kde(self):
        for item in self.ana_item:
            col1 = item + '_path1'
            col2 = item + '_path2'
        self.df_m[[col1, col2]].plot(kind='kde')
        plt.show()
class choose_model:
    def __init__(self,csv_path,id_list):
        pd.set_option('display.max_columns', 100000)
        pd.set_option('display.max_rows', 1000000)
        plt.style.use('ggplot')
        self.id_list = id_list
        self.csv_path = csv_path


    def compare(self):
        df = pd.read_csv(self.csv_path)
        df_select = df[df['ID'].isin(self.id_list)]
        fig, ax = plt.subplots(1, 1, figsize=(12, 12))
        # g = lambda x: x.set_ylim(0.8, 1)
        # g(axes[0][0])
        # g(axes[0][1])
        # g(axes[1][0])
        # g(axes[1][1])
        # ax.set_ylim(0.8, 1)
        df_select[['ID','P','R','mAP','F1']].plot.bar(ax=ax,x='ID',stacked=True)
        # df_select['R'].plot.bar(ax=axes[0][1],legend=True)
        # df_select['mAP'].plot.bar(ax=axes[1][0])
        # df_select['F1'].plot.bar(ax=axes[1][1])
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # ana2 = data_analyze_two(path1='../gray_warm_result_sean.csv',path2='../gray_result_sean.csv',ana_item=['mAP'])
    # ana2.kde()

    # test_item = ['far.data', 'mul.data', 'all.data', 'single_front.data', 'single_side.data']
    ana_item = ['backbone','optimizer','freeze_bn','freeze','weightDecay','LR']
    ana = data_analyze(path='/media/hkuit164/WD20EJRX/CNN_classification/result/underwater_action-4_class_result_laptop.csv',ana_item=ana_item,target_item='')
    ana.boxplot(ana_item)
    # for items in test_item:
    #     ana.test_means_dataset(items)
    # ana3 = choose_model(csv_path='/media/hkuit164/WD20EJRX/mysql/result/gray/gray_result_sean.csv',id_list=[1,2,6])
    # ana3.compare()