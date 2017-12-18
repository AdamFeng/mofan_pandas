import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# plot()画连续趋势图
# plot()参数详解：http://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html
data = pd.Series(np.random.randn(1000), index=np.arange(1000))

# 累加数据
data = data.cumsum()

data.plot()

plt.show()

data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list('ABCD')
)

data = data.cumsum()
data.plot()
plt.show()


################ 分割线 ###################

# scatter画散点图
ax = data.plot.scatter(x='A',y='B', color='DarkBlue', label='Class1')

# ax=ax 画到一张图中
data.plot.scatter(x='A',y='C', color='LightGreen', label='Class2', ax=ax)
plt.show()



############### 分割线 ###################

# pandas中其他画图方法：
# bar   条形图
# hist  
# box   箱图
# kde   
# area  
# scatter   散点图
# hexbin    
