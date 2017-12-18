import pandas as pd 
import numpy as np 

dates = pd.date_range('20140103', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])
print(df)
'''
             A   B   C   D
2014-01-03   0   1   2   3
2014-01-04   4   5   6   7
2014-01-05   8   9  10  11
2014-01-06  12  13  14  15
2014-01-07  16  17  18  19
2014-01-08  20  21  22  23
'''

print(df['A'])
print(df.A)
'''
选列，二者相同
2014-01-03     0
2014-01-04     4
2014-01-05     8
2014-01-06    12
2014-01-07    16
2014-01-08    20
Freq: D, Name: A, dtype: int32
'''

print(df[0:3])
'''
选行，切片
            A  B   C   D
2014-01-03  0  1   2   3
2014-01-04  4  5   6   7
2014-01-05  8  9  10  11
'''

# select by label:loc
print(df.loc['2014-01-05'])
'''
A     8
B     9
C    10
D    11
Name: 2014-01-05 00:00:00, dtype: int32
'''

print(df.loc[:,['A','B']])
'''
             A   B
2014-01-03   0   1
2014-01-04   4   5
2014-01-05   8   9
2014-01-06  12  13
2014-01-07  16  17
2014-01-08  20  21
'''

print(df.loc['2014-01-07',['A','B']])
'''
A    16
B    17
Name: 2014-01-07 00:00:00, dtype: int32
'''


# select by position:iloc
print(df.iloc[3])
'''
第三行
A    12
B    13
C    14
D    15
Name: 2014-01-06 00:00:00, dtype: int32
'''

print(df.iloc[3,1])
'''
13
'''

# mixed selection:ix
print(df.ix[:3, ['A','C']])
'''
            A   C
2014-01-03  0   2
2014-01-04  4   6
2014-01-05  8  10
'''

# Boolean indexing
print(df[df.A>8])
'''
             A   B   C   D
2014-01-06  12  13  14  15
2014-01-07  16  17  18  19
2014-01-08  20  21  22  23
'''