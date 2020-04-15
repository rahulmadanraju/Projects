# NLP-Search-Engine
NLP Powered Search Engine

### google_result.py - 

This file scrapes Google search result website title when provided a search query and the number of pages to scrape

### store_titles.py -

This file is a wrapper on top of the google_result.py that supplies it with a query and number of pages and stor them in "titles.csv"

### build_index.py -

Builds the index by doing some preprocessing on the titles first. Index is saved in 'index.pickle'

### load_index.py -

Run it - write down the related search query and it will present with a list of page titles that best match the query


### How to Run/Test -
```
python store_titles.py

python build_index.py

python load_index.py 

(When prompted to write the query write "How to learn Python for Data Science" or something related to python)
```