# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 00:50:58 2018

@author: rahul
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
#split the data to train and test
from sklearn.preprocessing import StandardScaler
#preprocessing the data
from sklearn.neighbors import KNeighborsClassifier
#type of the clasiifier being used
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
#last three steps for testing the data

#=============================================================================
dataset=pd.read_csv('C:/Users/rahul/Downloads/Datasets/KNN_Dataset.csv')
#=============================================================================
print("datalenghth", len(dataset))
print("data shape", dataset.shape)
print(dataset.head())
#=============================================================================
no_zeros=['Glucose', 'BloodPressure','SkinThickness', 'BMI', 'Insulin' ]

for column in no_zeros:
    dataset[column]=dataset[column].replace(0, np.NAN)
    mean= int(dataset[column].mean(skipna=True))
    dataset[column]=dataset[column].replace(np.NAN, mean)
#=============================================================================
X=dataset.iloc[:,0:8]
Y=dataset.iloc[:,8]
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,random_state=0, test_size=0.2)
print(X_train)
#=============================================================================
sc_x=StandardScaler()
X_train=sc_x.fit_transform(X_train)
X_test=sc_x.transform(X_test)
print(X_train)
#=============================================================================

# =============================================================================
classifier=KNeighborsClassifier(n_neighbors=11, metric='euclidean')
classifier.fit(X_train,Y_train)

# =============================================================================

y_pred=classifier.predict(X_test)
print(y_pred)
#=============================================================================

cm=confusion_matrix(Y_test, y_pred)
print(cm)
#=============================================================================
print(f1_score(Y_test, y_pred)*100)
#=============================================================================
print(accuracy_score(Y_test, y_pred)*100)