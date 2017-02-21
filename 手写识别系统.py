# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:38:45 2017

@author: chenshengkang
"""
import KNN
import os
import numpy as np

def img2vector(filename):
    returnVect = zeros((1,1024)) #创建1*1024的矩阵
    fr = open(filename) 
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect
            
def handwritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('trainingDigits') #获取目录内容
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    #获取训练集向量和标签
    for i in range(m):
        #解析文件名
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = os.listdir('testDigits')
    errorCount = 0
    mTest = len(testFileList)
    #获取测试集向量进行测试并将测试结果与正式结果比对
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = KNN.classify0(vectorUnderTest,trainingMat,hwLabels,3)
        print "the classifier came back with %d,the real answer is:%d" % (classifierResult,classNumStr)
        if classifierResult != classNumStr:
            errorCount += 1.0
    print '\n the total number of errors is：%d' % errorCount
    print '\n the total error rate is:%f' % (errorCount/float(mTest))
    
handwritingClassTest()
