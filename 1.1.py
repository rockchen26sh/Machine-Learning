# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:00:47 2017

@author: chenshengkang
"""

import numpy as np
from numpy import array
import operator

#import KNN

def createDataSet():
    group = array([1.0,1.1],[1.0,1.0],[0,0],[0,0.1])
    labels = ['A','A','B','B']
    return group,labels


#group,labels = KNN.createDataSet()

#group
#labels

#KNN.classify0([0.5,0.5],group,labels,3)


def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]    #训练集大小
    diffMat = np.tile(inX,(dataSetSize,1))-dataSet   
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    array0lines = fr.readlines()
    numberOfLines = len(array0lines)
    returnMat = np.zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in array0lines:
        line = line.strip()
        linstFromLine = line.split('\t')
        returnMat[index,:] = linstFromLine[0:3]
        classLabelVector.append(int(linstFromLine[-1]))
        index +=1
    return returnMat,classLabelVector

dataingDataMat,datingLabels = file2matrix('datingTestSet2.txt')

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataingDataMat[:,0],dataingDataMat[:,1],
           15.0*array(datingLabels),15.0*array(datingLabels))
plt.show

def autoNorm (dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals,(m,1))
    normDataSet = normDataSet/np.tile(ranges,(m,1))
    return normDataSet,ranges,minVals

normMat, ranges, minVals = autoNorm(dataingDataMat)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(normMat[:,0],normMat[:,1],
           15.0*array(datingLabels),15.0*array(datingLabels))
plt.show

def datingClassTest():
    hoRatio = 0.10
    dataingDataMat,datingLabels = file2matrix('datingTestSet.txt')
    normMat,ranges,minVals = autoNorm(dataingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],
                                     datingLabels[numTestVecs:m],3)
        print ("the classifier came back with : %d,the real answer is %d" % (classifierResult,datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print "the total error rate is : %f" % (errorCount/float(numTestVecs))

def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat , datingLables = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print "You will probably like this person:", resultList[classifierResult - 1]
classifyPerson()