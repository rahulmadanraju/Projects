@@ -0,0 +1,44 @@
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 00:25:57 2018

@author: rahul
"""
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris=load_iris()



print iris.feature_names
print iris.target_names
print iris.data[0]
print iris.target[0]




#the classification of training and testing data
test_idx=[0,50,99]



#training data
train_target=np.delete(iris.target,test_idx)
train_data=np.delete(iris.data,test_idx, axis=0)



#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]



#classification
clf=tree.DecisionTreeClassifier()
clf=clf.fit(train_data,train_target)

print test_target
print clf.predict(test_data)
