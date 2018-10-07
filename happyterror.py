
# coding: utf-8

# In[205]:


#dependencies
import pandas as pd
import numpy as np


# In[206]:


terror_csv ="C:/Users/randy/Desktop/Group_project/terrorism.csv"
df=pd.read_csv(terror_csv, encoding = "Latin")

df.head()


# In[207]:


new_df = df[["iyear","imonth", "country_txt", "region_txt", "city", "attacktype1_txt", "targtype1_txt","nkill","nwound"]]
new_df.head()


# In[208]:


df1=new_df.rename(index=str, columns={"iyear": "Year","imonth": "Month" , "country_txt": "Country", "region_txt": "Region" , "city": "City", "attacktype1_txt": "Attack Type" , "targtype1_txt": "Attack Type", "nkill": "Number Killed", "nwound": "Number Wounded"})


# In[209]:


df_new=df1.dropna()
df_new


# In[215]:


df_new.pivot_table(index='Year',values=['Number Killed','Number Wounded'])


# In[66]:


new_df.dtypes

