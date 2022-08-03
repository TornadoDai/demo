#!/usr/bin/env python
# coding: utf-8

# In[64]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from pylab import rcParams

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
data = pd.read_csv(r"C:\Users\12060\Downloads\exchange_rates.csv")
data1=data[['Series Description','CHINA -- SPOT EXCHANGE RATE, YUAN/US$ P.R. ']][5:]
data1.columns=['Date','YUAN/US$']
data1=data1.reset_index(drop=True)
data1
data2=data[['Series Description','HONG KONG -- SPOT EXCHANGE RATE, HK$/US$ ']][5:]
data2.columns=['Date','HK$/US$']
data2=data2.reset_index(drop=True)
data2
drop0=[]
for i in range(len(data1)):
    if data1.loc[i,'YUAN/US$']=='ND':
        drop0+=[i]
data1=data1.drop(index=drop0)
data1=data1.reset_index(drop=True)
item1=data1.copy()
item1.columns = ['ds','y']
item1.y = item1.y.astype('float')
item1.ds = item1.ds.astype('datetime64')
plt.figure(figsize=(20, 5), dpi=80)
plt.xlabel("Date")
plt.ylabel("Exchange Rate")
plt.plot(item1.ds, item1.y, label = 'yuan')

drop0=[]
for i in range(len(data2)):
    if data2.loc[i,'HK$/US$']=='ND':
        drop0+=[i]
data2=data2.drop(index=drop0)
data2=data2.reset_index(drop=True)
item2=data2.copy()
item2.columns = ['ds','y']
item2.y = item2.y.astype('float')
item2.ds = item2.ds.astype('datetime64')
plt.plot(item2.ds, item2.y, label = 'HK$')
plt.title("Comparison of exchange rate changes between China and Hong Kong against the US$")
plt.legend(loc = "best")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# In[ ]:





# In[ ]:




