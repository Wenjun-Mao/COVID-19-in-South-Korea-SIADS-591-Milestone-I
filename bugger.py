# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pandas.api.types import is_string_dtype, is_numeric_dtype

import datetime
import pixiedust

get_ipython().run_line_magic('matplotlib', 'inline')


# %%
df = pd.read_csv('.\data\PatientInfo.csv')
popinfo = pd.read_csv('.\data\Population.csv')
df = pd.merge(df, popinfo, on='province')



df['symptom_onset_date'] = pd.to_datetime(df['symptom_onset_date'])


# %%
# df['symptom_onset_date'] = pd.to_datetime(df['symptom_onset_date'], format = '%Y-%m-%d')
# df['symptom_onset_date'] = pd.to_datetime(df['symptom_onset_date'])
df['confirmed_date'] = pd.to_datetime(df['confirmed_date'], format = '%Y-%m-%d')
df['released_date'] = pd.to_datetime(df['released_date'], format = '%Y-%m-%d')
df['deceased_date'] = pd.to_datetime(df['deceased_date'], format = '%Y-%m-%d')
print(df.head(5))


# %%
print(df.info(), df.describe())


# %%
### 1. Know Your Data ###
# df.info()
# df.describe()

# missing values #
missing_count = df.isnull().sum() # the count of missing values
value_count = df.isnull().count() # the count of all values 
missing_percentage = round(missing_count / value_count * 100,2) #the percentage of missing values
missing_df = pd.DataFrame({'count': missing_count, 'percentage': missing_percentage}) #create a dataframe
print(missing_df)

# visualize missing value#
barchart = missing_df.plot.bar(y='percentage', figsize = (16,6), label = 'Missing-Percentage')
barchart.tick_params(labelrotation=30)
for index, percentage in enumerate(missing_percentage):
    barchart.text(index, percentage, str(percentage) + '%', horizontalalignment = 'center')


# %%



