# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:26:28 2020

@author: rahul
"""

import requests
import datetime
import pandas as pd
import csv

def write_csv(data):
    with open('output.csv', 'a', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, dialect = 'excel')
        writer.writerow(data)
        
def empty_row(file):
    header_names = ['title', 'domain', 'url', 'snippet','keyword','date']
    df = pd.read_csv(file, engine='python',sep=',', quotechar='"', error_bad_lines=False, header = None, skiprows = 1, names = header_names)
    df.dropna(axis=0, how='all',inplace=True)
    df.to_csv('output.csv', index=False)

# parameter used to search the data on google platform
params = {
  'access_key': '***************************', # API key
  'page' : 1, # 5 page search results are required
  'query': 'avoid cooling time and production costs for injection molding' # search using keywords
  }

api_result = requests.get('https://api.serpstack.com/search', params)

api_response = api_result.json()
    
for number, result in enumerate(api_response['organic_results'], start=1):
    # print ("%s. %s" % (number, result['title']))
    title = result['title']
    domain = result ['domain']
    url = result['url']
    snippet = result['snippet']
    keyword = params['query']
    date = datetime.datetime.now()
    lst = [title, domain, url, snippet, keyword, date]
    with open('output.csv','a', encoding = 'utf8') as outfile:
        writer = csv.writer(outfile, dialect = 'excel')
        writer.writerow(lst)
        
empty_row('output.csv')
