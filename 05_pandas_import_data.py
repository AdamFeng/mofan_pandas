import numpy as np 
import pandas as pd 

# http://pandas.pydata.org/pandas-docs/stable/io.html
# 读取：pd.read_???
# 存储：pd.to_???

# 读取csv
data = pd.read_csv('student.csv')

print(data)

data.to_pickle('student.pickle')