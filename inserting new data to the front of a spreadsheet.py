#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#load the excel file into a Pandas Data Frame

df = pd.read_excel('data/q.xlsx')

df_insert = pd.read_excel('data/r.xlsx') #depends on file type


# In[3]:


print(df)


# In[4]:


print(df_insert)


# In[5]:


#dataframe that needs to be changed . insert (location of column, new name of column, data to be inserted)

df.insert(loc = 0, column ='name_of_column',value = df_insert)
print(df)


# In[6]:


#export it back out into an excel file
df.to_excel('data/r_and_q.xlsx')

