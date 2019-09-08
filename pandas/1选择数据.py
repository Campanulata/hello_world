import numpy as np
import pandas as pd

dates = pd.date_range('20190101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

print(df)

print(df['A'],df.A)

print(df[0:3],df['20130102':'20130104'])