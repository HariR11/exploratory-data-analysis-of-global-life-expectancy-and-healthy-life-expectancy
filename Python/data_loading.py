#!/usr/bin/env python
# coding: utf-8

# # Data Loading
# 
# This notebook contains the steps for the loading the dataset and gathering info on the dataset
# 

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


# Load raw datasets
life_raw = pd.read_csv(r"90E2E48_ALL_LATEST.csv")
healthy_raw = pd.read_csv(r"C64284D_ALL_LATEST.csv")


# In[5]:


#viewing raw datasets
life_raw.head(5)


# In[6]:


healthy_raw.head(5)


# In[7]:


# Creating copies
life = life_raw.copy()
healthy = healthy_raw.copy()


# In[8]:


# checking shape 
print("Life expectancy raw:", life_raw.shape)
print("Healthy life expectancy raw:", healthy_raw.shape)

print("Life expectancy working copy:", life.shape)
print("Healthy life expectancy working copy:", healthy.shape)


# In[9]:


#checking columns
print("Life expectancy columns:")
print(life.columns.tolist())

print("\nHealthy life expectancy columns:")
print(healthy.columns.tolist())

print("\nLife expectancy sample:")
print(life.head())

print("\nHealthy life expectancy sample:")
print(healthy.head())


# In[10]:


# Checking data types

print("Life expectancy data types:")
print(life.dtypes)

print("\nHealthy life expectancy data types:")
print(healthy.dtypes)

