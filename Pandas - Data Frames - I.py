#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from numpy.random import randn


# In[3]:


#random seed value is provided to get same random number(random numbers generator type i. seed ii. linear congurential etc.)
np.random.seed(101)


# In[7]:


#data frame is created using randn function of numpy array to generate required 2D matrix
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[5]:


df#here W,X,Y & Z are just simple series of pandas that shares a common index(A,B,C,D,E)


# In[6]:


df['W']#if we fetch coloumns individually we can see the demonstration of collection of series in DataFrames


# In[9]:


type(df['W'])#series demo


# In[11]:


type(df)#DataFrame demo


# In[12]:


#another way of fetching the whole column is how we do in SQL
df.W


# In[14]:


df.X#it is always recomended to use rectangular braces method as df. is mainly used to implement dataframe functions


# In[17]:


#fetching multiples columns as once from a dataframe(using double square braces)
df[['W','X']]


# In[28]:


#creating or adding a new column using mathematical operations on existing columns
df['N'] = df['W'] + df['Y']


# In[29]:


df


# In[30]:


#removing a column from the data frame using drop(to drop a column axis=1 must be defined as axis=0 refers to the index
# else it will show up a value error mentioning that the required column is not contained in the axis or the index)
df.drop('N',axis=1)
#but droping as above wont make any changes to the original dataframe or actual inplace therefore inplace must be defined\


# ###### axis=0 ==> Rows |axis=1 ==>Columns
#     - because in shape of a matrix(row,column) index of row=0, col=1

# In[31]:


#checking if the column is actually dropped from the dataframe or not
df
#its not so lets define inplace changes to true so that the original dataframe will actually get effected


# In[34]:


#now the column will be permanently removed from the original dataframe
df.drop('N',axis=1,inplace=True) 


# In[32]:


df


# In[35]:


#Fetching a row from the DataFrame 
#normal loc function
df.loc['C']


# In[36]:


#index based loc i.e. iloc
df.iloc[2]


# In[37]:


#fetching values corresponding to both row and column
df.loc['A','X']


# In[38]:


#creating the subset of the dataframe
df.loc[['A','B'],['X','Y']]


# In[ ]:




