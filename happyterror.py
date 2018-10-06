
# coding: utf-8

# In[58]:


#dependencies
import pandas as pd
import numpy as np


# In[59]:


terror_csv ="C:/Users/randy/Desktop/PREWORK/global_terrorism.csv"
df=pd.read_csv(terror_csv, encoding = "Latin")
df.head()


# In[60]:


new_df = df[["iyear","imonth", "country_txt", "region_txt", "city", "attacktype1_txt", "targtype1_txt","nkill","nwound"]]
new_df.head()


# In[62]:


new_df.dtypes

