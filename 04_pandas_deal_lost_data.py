import numpy as np 
import pandas as pd 

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

print(df)
'''
             A     B     C   D
2013-01-01   0   NaN   2.0   3
2013-01-02   4   5.0   NaN   7
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
'''

df_clean = df.dropna(
    axis=0, # 0：对行进行操作，1：对列进行操作
    how='any' # 'any'：只要存在NaN就drop，'all'：全部是NaN才drop
)

# 使用0代替NaN
df_clean = df.fillna(value=0)

print(df_clean)

# 判断是否有缺失数据 NaN, 为 True 表示缺失数据
print(df.isnull())
'''
                A      B      C      D
2013-01-01  False   True  False  False
2013-01-02  False  False   True  False
2013-01-03  False  False  False  False
2013-01-04  False  False  False  False
2013-01-05  False  False  False  False
2013-01-06  False  False  False  False
'''

# 检测在数据中是否存在 NaN, 如果存在就返回 True
print(np.any(df.isnull()))