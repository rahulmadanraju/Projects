import pandas as pd 
pd.set_option('display.max_colwidth', -1)
import numpy as np
from nltk import word_tokenize
import multiprocessing
import time
import string
import pickle
from six import string_types
pd.set_option('display.expand_frame_repr', False)
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import warnings
warnings.filterwarnings('ignore')

global index
index = {}

df = pd.read_csv('titles.csv')
df['processed'] = ""

def preprocess(text):
    text = text.translate(str.maketrans('','', string.punctuation))
    text = text.lower()
    text = word_tokenize(text)
    new_text = []
    for word in text:
        word = str(word)
        lemmatized = lemmatizer.lemmatize(word,'n')
        lemmatized = lemmatizer.lemmatize(lemmatized,'v')
        new_text.append(lemmatized)
    return new_text

def add_word_to_index(word, index_no):
    if word not in index:
        index[word] = [index_no]
    else:
        if index_no not in index[word]:
            index[word].append(index_no)

def index_title(text, index_no):
    for word in text:
        word = str(word)
        if not len(word)==1:
            add_word_to_index(word, index_no)

for no, row in df.iterrows():
    text = row['Titles']
    text = preprocess(text)
    df.set_value(no, 'processed', " ".join(text))
    index_title(text, no)
    
# documents = list(set().union(index['lyndacom'],index['youtube']))

df.to_csv('titles.csv', index=False)

with open('index.pickle','wb') as f:
    pickle.dump(index, f, pickle.HIGHEST_PROTOCOL)

