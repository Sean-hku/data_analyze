import pandas as pd

df=pd.read_csv('5_train.xlsx')
# print(df)
df.insert(df.shape[1],'model_num','5')
df.drop(['Unnamed_0'],axis=1,inplace=True)
print(df)
df.to_csv('5_train.xlsx')
# print(df)