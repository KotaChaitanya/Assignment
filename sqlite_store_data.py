# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:32:50 2019

@author: ck186026
"""

import sqlite3
import pandas as pd

con = sqlite3.connect("database.db")

metadata = pd.read_csv('metadata.csv', sep = ',')
metadata.to_sql("metadata", con, if_exists="replace")
print(metadata.info())

data = pd.read_csv('data.csv', sep = ',')
data.to_sql("data", con, if_exists="replace")
print(data.info())

#res = pd.read_sql_query("select * from metadata where location= 'Perimeter'", con)
#print(res)