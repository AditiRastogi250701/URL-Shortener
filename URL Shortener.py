#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyshorteners')


# In[2]:


import pyshorteners


# In[3]:


link=input()


# In[4]:


shortener=pyshorteners.Shortener()


# In[5]:


shortened_link=shortener.tinyurl.short(link)


# In[6]:


print("Shortened Link ",shortened_link)

