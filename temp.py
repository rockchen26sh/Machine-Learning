# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
os.chdir('/home/laptop/github/Machine-Learning')
#load data
df = pd.read_csv('train.csv')
#data spilt
train_label = df.label
train_data = df.ix[:,1:] 
#convert to np
train_data = np.array(train_data)
train_label = np.array(train_label)
#KNN model
knn = KNeighborsClassifier(n_neighbors=5,weights='distance') #K_Value:5

#KNN训练分类器
knn.fit(train_data,train_label)

#test_data load
df = pd.read_csv('test.csv')
test_data = np.array(df)

#predict
result = knn.predict(test_data)

Series(result).to_csv('result.csv')
