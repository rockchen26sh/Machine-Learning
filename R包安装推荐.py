# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:05:44 2017

@author: chenshengkang
"""

import pandas as pd
import numpy as np
import os
os.getcwd()
data = pd.read_csv('installations.csv')
data[:5]
grouped = data.groupby(['Package','User']).sum()
data2 = grouped.unstack('Package')
data2
similarities = np.corrcoef(data2)
distances = log((similarities/2)+0.5)
distances




def neighbors(i,distances,k):
    result = distances.sort(columns = (i-1))[i-1]
    result = result[:k]
    return result

neighbors(1,distances,25)

def installation_probability(user,package,matrix,distances,k):
    neighbors = neighbors(package,distances,k)
    mean_temp = []    
    for neighbor in range(0,len(neighbors)):
        mean_temp.append(matrix[user,neighbor])
    return np.mean(mean_temp)

installation_probability(1,1,data2,distances,25)

neighbors1 = neighbors(1,distances,25)
[np.mean(data2[1,x]) for x in neighbors1]
neighbors1.index[1]
data2.ix[neighbors1.index[1],:]
data2.ix