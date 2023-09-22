#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import math


# In[5]:


file_path = "C:\\Users\\ayush\\OneDrive\\Desktop\\ayush\\EPL dataset\\premier_league_22-23.csv"

# Read the CSV file into a DataFrame
epl = pd.read_csv(file_path)


# In[6]:


epl


# In[7]:


epl.info()


# In[9]:


GK = 'GKRating'

sorted_GK = epl.sort_values(by=GK, ascending=False)
sorted_GK = sorted_GK.reset_index(drop=True)
#Best Goalkeepers in Premier league
print(sorted_GK)


# In[10]:


#Most players from which nation

nationality = epl.groupby('NationalTeam').size().sort_values(ascending=False)
nationality.head(10).plot(title= 'No. of players by Nation', kind= 'bar', figsize= (12,6), color=sns.color_palette('magma'))


# In[12]:


under_20= epl[epl['Age']<20.0]
age20_25= epl[(epl['Age']>=20.0) & (epl['Age']<=25.0)]
age26_30= epl[(epl['Age']>25.0) & (epl['Age']<=30.0)]
above_30= epl[epl['Age']>30.0]


# In[13]:


x= np.array([under_20['Age'].count(), age20_25['Age'].count(), age26_30['Age'].count(), above_30['Age'].count()])
agelabels= ['<20','20-25','26-30','<30']
plt.title('Player Age Groups', fontsize=16)
plt.pie(x, labels=agelabels, autopct='%.1f%%')
plt.show

#Player of different age groups in English Premier league


# In[18]:


under_20[epl['Club']=='Newcastle United']
#Players with age less 20 playing for Newcastle United.


# In[19]:


player_num= epl.groupby('Club').size()
data= (epl.groupby('Club')['Age'].sum()) / player_num
data.sort_values(ascending=False)
#Average age of each clubs


# In[27]:


#Top 10 Potential at FIfa 23
top_10_ast= epl[['FullName','Club','Potential','Age']].nlargest(n=10, columns='Potential')
top_10_ast


# In[32]:


#Best Passer in premier league


best_passer=epl[['FullName','PassingTotal','Age','Potential']].nlargest(n=20,columns='PassingTotal')
best_passer


# In[ ]:


## Surprisingly ederson is in second place.


# In[35]:


Avg_contact_expired= int(np.sum(epl['ContractUntil']))/695
Avg_contact_expired
#Avg 4 year contract


# In[42]:


chelsea_players=epl[['FullName','Club']]
desired_string = "Chelsea"
result = [row[1] for row in chelsea_players if row[1] == desired_string]

# Convert the list to a NumPy array (if needed)
result=np.array(result)


# In[ ]:




