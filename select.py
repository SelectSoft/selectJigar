# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 00:32:53 2019

@author: Saifullah
"""

import pyodbc 
import pandas as pd


cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-Q98TBPV;"
                      "Database=SelectFashion;"
                      "Trusted_Connection=yes;")

    
    
product = pd.read_sql_query("select *  from Product", cnxn)



images = pd.read_sql_query("select *  from productimage", cnxn)





