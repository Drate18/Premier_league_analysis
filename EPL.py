#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import math


# In[6]:


file_path = "C:\\Users\\ayush\\OneDrive\\Desktop\\ayush\\EPL dataset\\epl_results_2022-23.csv"

# Read the CSV file into a DataFrame
epl = pd.read_csv(file_path)


# In[7]:


epl.head()


# In[8]:


epl.info()


# In[9]:


display(epl.describe())


# In[10]:


epl


# In[14]:


Total_Goals = int(np.sum(epl['FTAG']))+int(np.sum(epl['FTHG']))
#Total Goals scored in all the matches combined
#FTAG->Full Time Away Goals
#FTHG->Full Time Home Goals
print('Total Goals Scored in 2022/23:', Total_Goals)


# In[17]:


epl.FTR

