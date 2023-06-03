#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib

model = joblib.load('music-recommender.joblib')
predictions = model.predict([ [21,1], [22, 0] ])
predictions

