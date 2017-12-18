import numpy as np 
import pandas as pd 

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])

print(df)
'''
             A   B   C   D
2013-01-01   0   1   2   3
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
'''

# 根据索引或者标签修改值
df.iloc[2,2] = 1111
df.loc['2013-01-01','B'] = 222

# 根据条件修改值
df.A[df.A>8] = 0

# 新增列
df['F'] = np.nan
df['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101', periods=6))

print(df)
'''
            A    B     C   D   F  E
2013-01-01  0  222     2   3 NaN  1
2013-01-02  4    5     6   7 NaN  2
2013-01-03  8    9  1111  11 NaN  3
2013-01-04  0   13    14  15 NaN  4
2013-01-05  0   17    18  19 NaN  5
2013-01-06  0   21    22  23 NaN  6
'''