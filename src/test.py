import os 
import pandas as pd 

from datetime import datetime
from datetime import timedelta
import time

# 현재 경로 확인 
print(os.getcwd())

files = os.listdir('./data/input')[:-3] # -3을 한 이유 -> 잘못받아와서 

for num, file in enumerate(files):
    print(file)
    # print(len(file))
    path = f'./data/input/{file}'
    print(path)
    # for idx in range(len(files)):
    #     print(idx)
    #     path = f'./data/input/{files[idx]}'
    #     print(path, len(path))
    df   = pd.read_excel(path, encoding='utf-8')
    # print(df.head(2))
    # 년도 추출 
    year = file[:4]
    print(year) 
    print('='*100,'log_1')   
    drop_col = df.loc[:4-1,:]
    df = drop_col.iloc[[0,2,3],:]
    print(df)
    print('='*100,'log_2')   
    # 사본
    df_t = df.iloc[:]
    # 돌리기 
    df_t = df.T
    print(df_t.head(5))
    print('='*100,'log_3')  
    df_t= df_t.reset_index()
    # df_t.info()
    # df_t[3][1]
    cols_dic = {df_t.columns[0]:'date',
       df_t.columns[1]:'avg',
       df_t.columns[2]: df_t[2][1],
       df_t.columns[3]: df_t[3][1]}
    # print(cols_dic)
    df_t.rename(columns=cols_dic, inplace=True)
    del_cols = df_t.index[:2]
    df_t.drop(index=del_cols, inplace=True)
    df_t= df_t.reset_index()
    # print(df_t)
    df_t.drop('index',axis=1,inplace=True )
    print(df_t)
    print('='*100,'log_3')
    for idx, i in enumerate(df_t.date):
        print(i)
    #     print(df_t.date[idx])
        if i.month >= 10:
            month = str(i.month)
            df_t.date[idx]= year+'-'+month
            print(month, df_t.date[idx])
        else:
            month = "0"+str(i.month)
            df_t.date[idx]= year+'-'+month
            print(month, df_t.date[idx])
    print(df_t)
    print('='*100,'log_4')
    df = df_t.T
    print(df)
    # print(files[1][:17])
    name = files[num][:17]
    print(name)

    df.to_csv(f'./data/output/{name}.csv', encoding='euc-kr', index=False)