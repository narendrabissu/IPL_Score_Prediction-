#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


with open(r'C:\Users\HP\all_matches.csv','r') as f :
    
    
    ipl_data=pd.read_csv(f)


# In[3]:


print(ipl_data.columns)


# In[4]:


relevantcolumns=['match_id','venue','innings','ball','batting_team','bowling_team','striker','non_striker','bowler','runs_off_bat','extras','wides','noballs','byes','legbyes','penalty']


# In[5]:


ipl_data=ipl_data[relevantcolumns]


# In[6]:


ipl_data['total_runs']=ipl_data['runs_off_bat']+ipl_data['extras']


# In[7]:


ipl_data.drop(columns=['runs_off_bat','extras'])


# In[8]:


ipl_data=ipl_data[ipl_data['ball']<=5.6]


# In[9]:


ipl_data=ipl_data[ipl_data['innings']<=2]


# In[10]:


ipl_data.head(50)


# In[11]:


#pd.value_counts(ipl_data.striker)


# In[12]:


ipl_data=ipl_data.groupby(['match_id','venue','innings','batting_team','bowling_team']).agg({"total_runs":"sum","striker":"nunique"})


# In[13]:


ipl_data.head()


# In[14]:


ipl_data=ipl_data.rename(columns={'striker':'wickets'})


# In[15]:


ipl_data.tail()


# In[16]:


ipl_data=ipl_data.reset_index()


# In[17]:


ipl_data=ipl_data.drop(columns=['match_id'])


# In[18]:


ipl_data.to_csv("mypreprocessed.csv",index=False)


# In[19]:


ipl_data.head()


# In[ ]:





# In[ ]:




