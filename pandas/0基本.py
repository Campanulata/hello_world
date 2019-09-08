import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1])
# 列表
print(s)

dates = pd.date_range('20190101',periods=6)
# index
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
# 矩阵
print(df)

df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

print(df1.describe())
# 快速分析

print(df1.T)

df1.sort_index(axis=1,ascending=False)
# 排序标签

df1.sort_values(by='E')
# 值排序            选定列
