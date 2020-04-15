import pickle
import pandas as pd
pd.set_option('display.max_colwidth', -1)
from nltk import word_tokenize
import string
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.metrics import edit_distance
lemmatizer = WordNetLemmatizer()
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
df = pd.read_csv('titles.csv')

def edit_percentage(text1, text2):
    distance = float(edit_distance(text1, text2))
    totallength = len(text1) + len(text2)
    distance = (totallength - distance)/totallength*100.0
    return distance

def preprocess(text):
    text = str(text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()
    text = word_tokenize(text)
    new_text = []
    for word in text:
        word = lemmatizer.lemmatize(word,'n')
        word = lemmatizer.lemmatize(word,'v')
        new_text.append(word)
    return new_text

def cosine_similarity(title, query):
    title = title.strip()
    query = query.strip()
    tfidf = vectorizer.fit_transform([title.lower(),query.lower()])
    return ((tfidf * tfidf.T).A)[0,1]

with open('index.pickle','rb') as f:
    index = pickle.load(f)

def get_suggestions(text):
    index_frame = pd.DataFrame()
    index_frame['Indexes'] = index.keys()
    index_frame['Edit Values'] = index_frame['Indexes'].apply(lambda x: edit_percentage(x, text))
    a, b = index_frame.sort_values(by=['Edit Values'], ascending = [False]).reset_index(drop=True).ix[0]
    return a

def process_query(query):
    query_token_frame = pd.DataFrame()
    query_token_frame['tokens'] = query.split()
    query = preprocess(query)
    bigarray = []
    craft_token = []
    suggestion_required = 0
    for count, token in enumerate(query, start=0):
        try:
            bigarray.append(index[token])
            craft_token.append(query_token_frame['tokens'].ix[count])
        except:
            suggestion_required = 1
            suggestion = get_suggestions(token)
            craft_token.append(suggestion)
    if (suggestion_required == 1):
        suggestion_answer = input("Did you mean '" + " ".join(craft_token) + "' ? ")
        if suggestion_answer == 'Yes':
            process_query(" ".join(craft_token))
        else:
            get_results(query, bigarray)
    else:
        get_results(query, bigarray)

def get_results(query, bigarray):
    documents = list(set().union(*bigarray))
    frame = pd.DataFrame()
    frame['actual'] = df.loc[documents].Titles.reset_index(drop=True)
    frame['processed'] = df.loc[documents].processed.reset_index(drop=True)
    frame['cosine_similarity'] = frame.processed.apply(lambda x: cosine_similarity(x, " ".join(query)))
    print(frame.sort_values(by=['cosine_similarity'], ascending = [False])['actual'].reset_index(drop=True))

query = input("Enter you search query? ")
process_query(query)




