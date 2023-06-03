#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns = ['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X,y)
joblib.dump(model, 'music-recommender.joblib') #save the model to file with choice of name
#predictions = model.predict([ [21,1], [22, 0] ]) # provided custom values for testing not good practice

