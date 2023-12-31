# -*- coding: utf-8 -*-
"""Bike share demand.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iHsoweNshNpDDZQNqUhji0WMuSUaVqgC
"""

import pandas as pd

df=pd.read_csv("/content/train(1).csv")
df_test=pd.read_csv("/content/test.csv")

import matplotlib.pyplot as plt
import seaborn as sns

df.head()

df_test.head()

df.drop(columns = ['casual','registered'],inplace = True)

print('df Dataframe:')
print(df.dtypes)
print()
print('df_test DataFrame:')
print(df_test.dtypes)

df['datetime'] = pd.to_datetime(df['datetime'])
df[['season', 'weather']] = df[['season', 'weather']].astype(str)
df_test['datetime'] = pd.to_datetime(df_test['datetime'])
df_test[['season', 'weather']] = df_test[['season', 'weather']].astype(str)

df.duplicated().sum()

df.isna().sum() * 100 / df.shape[0], df_test.isna().sum() * 100 / df_test.shape[0]

plt.figure(figsize = (7.5, 2.5))
plt.title('Boxplot - Count')
ax = sns.boxplot(data = df, x = 'count')
ax.set_xlabel('')
plt.show()

import numpy as np
from scipy import stats

for i in [df, df_test]:
    i['year'] = i['datetime'].dt.year
    i['month'] = i['datetime'].dt.month
    i['day'] = i['datetime'].dt.day
    i['day_of_week'] = i['datetime'].dt.dayofweek
    i['hour'] = i['datetime'].dt.hour

df.drop(columns = 'datetime', inplace = True)

plt.figure(figsize = (7.5, 2.5))
plt.title('Histogram - Count')
ax = sns.histplot(data = df, x = 'count', kde = True)
plt.show()