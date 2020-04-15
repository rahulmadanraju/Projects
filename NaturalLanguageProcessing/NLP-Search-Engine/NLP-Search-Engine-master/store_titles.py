# -*- coding: utf-8 -*-
from google_result import search
from bs4 import BeautifulSoup
import pandas as pd


webpages = search("How to learn python", 4)

titles = []

for result in webpages:
	titles.append(result[0].replace("  "," "))

print(titles)
df = pd.DataFrame()
df['Titles'] = titles
df.to_csv('titles.csv', index=True)
