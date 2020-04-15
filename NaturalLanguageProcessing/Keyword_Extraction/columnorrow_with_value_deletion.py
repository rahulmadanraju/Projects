# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:47:38 2020

@author: rahul
"""

# delete the particular column containing irrelevant data

indexNames = data[data['columnname'] == 'Value_in_Column'].index
 
# Delete these row indexes from dataFrame
dataNew.drop(indexNames , inplace=True)