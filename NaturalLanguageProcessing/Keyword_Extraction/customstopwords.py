# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:17:33 2020

@author: rahul
"""

# creating additional stopwords for the existing stopwords

##Creating a list of stop words and adding custom stopwords
stop_words = set(stopwords.words("english"))
##Creating a list of custom stopwords
new_words = ["using", "show", "result", "large", "also", "iv", "one", "two", "new", "previously", "shown"]
stop_words = stop_words.union(new_words)