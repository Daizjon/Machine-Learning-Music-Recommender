#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_data = pd.read_csv('music.csv')
#split into input and output
#drop removes a column from a data set, since we want age and gender as input we will drop genre from the data set
X = music_data.drop(columns = ['genre'])
#X #show X data set
#gets genre column
y = music_data['genre']
#y #show y data set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.2) #allocates 20 percent of our data for testing

model = DecisionTreeClassifier()
#model.fit(X,y) #takes two data sets input and output #passes entire data set which is not good 
#want to pass trained data set
model.fit(X_train,y_train)
#predictions = model.predict([ [21,1], [22, 0] ]) # provided custom values for testing not good practice
predictions = model.predict(X_test)
#now want to compare prediction accuracy which compares xtest to ytest
#predictions
score = accuracy_score(y_test, predictions) #returns accuracy score between 0 and 1
score

