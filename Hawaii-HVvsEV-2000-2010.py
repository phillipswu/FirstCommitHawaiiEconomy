#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns


# In[24]:


df = pd.read_csv('HAWAII Registered EV and HV Vehicles-2000-2010.csv', index_col="Year", parse_dates=True)


# In[67]:


plt.title("Maui Electric Vehicle vs. Hybrid Vehicle Ownership")


# In[66]:


sns.lineplot( data=df)
sns.set_style("dark")

legend=False
plt.legend(title='Electric vs. Hybrid', loc='upper right', labels=['EV', 'HV'])


# In[63]:


plt.xlabel("Year",fontsize=14)
plt.ylabel("Total Vehicles",fontsize=14)
plt.xlim(1999, 2010)
plt.ylim(0 ,1000)


# In[69]:


sns.lineplot(data=df['EV'], label="Electric Vehicles")
sns.lineplot(data=df['HV'], label="Hybrid Electric Vehicles")
plt.show()


# In[ ]:




