# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 11:00:27 2018

@author: rahul
"""

import numpy as np
#used for mathematical computations
import pandas as pd
#used for data structuring and analysis
from sklearn.cross_validation import train_test_split
#used for spliting the dataset to train and test
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

file_name='C:/Users/rahul/Downloads/Decision_Tree_ Dataset_Decision_Tree_ Dataset_1.csv'
read_data=pd.read_csv(file_name, sep=',', header=0)

print("dataset Length::", len(read_data))
#len is used for giving the length of the dataset
print("dataset <shape::", read_data.shape)
#shape is used for giving the shape of the dataset

print("dataset", read_data.head)
#head command is used to view the details of internal contents.

X= read_data.values[:,1:6]
print(X)
Y= read_data.values[:,0]
print(Y)
#X=X.astype('float32')
#seperate the target variable

#Y=Y.astype('int')
#the error will be thrown for y data if the data_type of y is not mentioned. 


X_train, X_test, Y_train, Y_test= train_test_split(X, Y, test_size= 0.3, random_state= 100)
#split the data to train set and test set
'''print(X_train)
print(Y_train)
print(X_test)
print(Y_test)'''


clf_entropy= DecisionTreeClassifier(criterion="entropy",random_state=100, max_depth=160, min_samples_leaf=20)
clf_entropy.fit(X_train, Y_train)

y_pred_en=clf_entropy.predict(X_test)
print(y_pred_en)


print("accuracy is:"), accuracy_score(Y_test, y_pred_en)*100
