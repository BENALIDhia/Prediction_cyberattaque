#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np


# In[9]:


data1=pd.read_csv('C:/Users/MSI/Desktop/Stage Caplogy/NEW DATASET/CSV-03-11/03-11/LDAP.csv')


# In[10]:


data2=pd.read_csv('C:/Users/MSI/Desktop/Stage Caplogy/NEW DATASET/CSV-03-11/03-11/MSSQL.csv')


# In[11]:


data3=pd.read_csv('C:/Users/MSI/Desktop/Stage Caplogy/NEW DATASET/CSV-03-11/03-11/NetBIOS.csv')


# In[12]:


data4=pd.read_csv('C:/Users/MSI/Desktop/Stage Caplogy/NEW DATASET/CSV-03-11/03-11/Portmap.csv')


# In[13]:


data5=pd.read_csv('C:/Users/MSI/Desktop/Stage Caplogy/NEW DATASET/CSV-03-11/03-11/Syn.csv')


# In[14]:


data6=pd.read_csv('C:/Users/MSI/Desktop/Stage Caplogy/NEW DATASET/CSV-03-11/03-11/UDP.csv')


# In[15]:


data7=pd.read_csv('C:/Users/MSI/Desktop/Stage Caplogy/NEW DATASET/CSV-03-11/03-11/UDPLag.csv')


# In[16]:


data1.columns


# In[28]:


# Combinez les ensembles de données
npdata = np.concatenate((data1[' Timestamp'],data2[' Timestamp'],data3[' Timestamp'],data4[' Timestamp'],data5[' Timestamp'],data6[' Timestamp'],data7[' Timestamp']), axis=0)


# In[31]:


data = pd.DataFrame(npdata, columns=[['Timestamp']])


# In[32]:


data.head(10)


# In[36]:


# Sauvegarder le DataFrame en CSV
data.to_csv('C:/Users/MSI/Desktop/Stage Caplogy/NEW DATASET/CSV-03-11/03-11/data_combined.csv', index=False)


# In[ ]:




