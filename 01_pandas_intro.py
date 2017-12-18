'''
如果用 python 的列表和字典来作比较, 
那么可以说 Numpy 是列表形式的，没有数值标签，
而 Pandas 就是字典形式。
Pandas是基于Numpy构建的，让Numpy为中心的应用变得更加简单。
'''

import pandas as pd 
import numpy as np 

s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)
'''
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
Series的字符串表现形式为：索引在左边，值在右边。
由于没有为数据指定索引，所以会自动创建一个0到N-1（N为长度）的整数型索引。
'''

# 用来当行索引
dates = pd.date_range('20170707',periods=6)
print(dates)
'''
DatetimeIndex(['2017-07-07', '2017-07-08', '2017-07-09', '2017-07-10',
               '2017-07-11', '2017-07-12'],
              dtype='datetime64[ns]', freq='D')
'''

# index行索引   columns列索引
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['a','b','c','d'])
print(df)
'''
                   a         b         c         d
2017-07-07  0.118444  0.435465 -0.121211 -0.105744
2017-07-08 -1.313554  0.615423 -0.608361  0.887515
2017-07-09 -1.221020 -2.219393 -0.514167 -0.052783
2017-07-10 -0.488934  0.831327 -0.565232 -0.315700
2017-07-11 -0.194622 -0.967104  0.576797  1.826064
2017-07-12 -1.421902 -0.151822 -1.102552 -0.269886
DataFrame是一个表格型的数据结构，它包含有一组有序的列，每列可以是不同的值类型
（数值，字符串，布尔值等）。
DataFrame既有行索引也有列索引， 它可以被看做由Series组成的大字典。
'''
print(df['b'])
'''
2017-07-07    0.180182
2017-07-08    1.122290
2017-07-09   -1.094093
2017-07-10    0.812743
2017-07-11   -0.475577
2017-07-12    1.719212
Freq: D, Name: b, dtype: float64
'''

# 不指定index和columns，默认索引从0开始
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)
'''
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''

df2 = pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20170303'),
    'C':pd.Series(1, index=list(range(4)), dtype='float32'),
    'D':np.array([3]*4, dtype='int32'),
    'E':pd.Categorical(['test', 'train', 'test', 'train']),
    'F':'foo'
})
print(df2)
'''
     A          B    C  D      E    F
0  1.0 2017-03-03  1.0  3   test  foo
1  1.0 2017-03-03  1.0  3  train  foo
2  1.0 2017-03-03  1.0  3   test  foo
3  1.0 2017-03-03  1.0  3  train  foo
这种方法能对每一列的数据进行特殊对待。
'''

# 每一列数据的数据类型
print(df2.dtypes)
'''
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
'''

print(df2.index)
'''
行索引
Int64Index([0, 1, 2, 3], dtype='int64')
'''

print(df2.columns)
'''
列索引
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
'''

print(df2.values)
'''
[[1.0 Timestamp('2017-03-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2017-03-03 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2017-03-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2017-03-03 00:00:00') 1.0 3 'train' 'foo']]
'''

print(df2.describe())
'''
只能运算数字格式的统计信息
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
'''

print(df2.sort_index(axis=1, ascending=False))
'''
按照列索引从大到小排序
     F      E  D    C          B    A
0  foo   test  3  1.0 2017-03-03  1.0
1  foo  train  3  1.0 2017-03-03  1.0
2  foo   test  3  1.0 2017-03-03  1.0
3  foo  train  3  1.0 2017-03-03  1.0
'''

print(df2.sort_index(axis=0, ascending=False))
'''
按照行索引从大到小排序
     A          B    C  D      E    F
3  1.0 2017-03-03  1.0  3  train  foo
2  1.0 2017-03-03  1.0  3   test  foo
1  1.0 2017-03-03  1.0  3  train  foo
0  1.0 2017-03-03  1.0  3   test  foo
'''

print(df2.sort_values(by='E'))
'''
按照列的数据值排序
     A          B    C  D      E    F
0  1.0 2017-03-03  1.0  3   test  foo
2  1.0 2017-03-03  1.0  3   test  foo
1  1.0 2017-03-03  1.0  3  train  foo
3  1.0 2017-03-03  1.0  3  train  foo
'''