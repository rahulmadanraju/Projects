# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:16:18 2019

@author: rahul
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re  #library used to clean the texts
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


# Importing the dataset, tab seprated dataset is loaded, using the quoting = 3, we are removing the double quotes
data = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)
nltk.download('stopwords') #stopswors used to remove the irrelevant words
corpus = []

# Texts are cleaned to get only relevant words and remove the reduntant info e.g.:..., the, I etc.
for i in range(0,1000):
    
    review = re.sub('[^a-zA-Z]',' ', data['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
# Bag of words model
cv = CountVectorizer(max_features = 1000)
X = cv.fit_transform(corpus).toarray()
y = data.iloc[:, 1].values

# Data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Using the Naive Bayes Classifier
classifierNB = GaussianNB()
classifierNB.fit(X_train, y_train)

y_pred = classifierNB.predict(X_test)
accuracyNB = accuracy_score(y_test, y_pred)
cmNB = confusion_matrix(y_test, y_pred)

# Using the Decision Tree Classifier
classifierDT = DecisionTreeClassifier()
classifierDT.fit(X_train, y_train)

y_pred = classifierDT.predict(X_test)
accuracyDT = accuracy_score(y_test, y_pred)
cmDT = confusion_matrix(y_test, y_pred)

# Using the SVM Classifier
classifierSVM = SVC( degree=3, kernel = 'rbf', random_state=None, gamma ='auto' )
classifierSVM.fit(X_train, y_train)

y_pred = classifierSVM.predict(X_test)
accuracySVM = accuracy_score(y_test, y_pred)
cmSVC = confusion_matrix(y_test, y_pred)
