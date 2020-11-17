#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import matplotlib as plt
import seaborn as sns

master_table = pd.read_csv ('conposcovidloc.csv', index_col=0)

master_table.head()


# In[63]:


client_gender_plot = sns.countplot(data = master_table, x = "Client_Gender")


# In[32]:


age_plot = sns.countplot(data = master_table, x = "Age_Group")


# In[68]:



city_plot = sns.countplot(x=("Reporting_PHU_City"),
                          data=master_table, order=master_table['Reporting_PHU_City'].value_counts().iloc[:10].index)
city_plot.set_xticklabels(city_plot.get_xticklabels(), rotation=30, ha="right", fontsize=10)
city_plot


# In[43]:




