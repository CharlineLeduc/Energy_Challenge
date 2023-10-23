# -*- coding: utf-8 -*-
"""
Spyder Editor




#TEST


This is a temporary script file.
"""
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 


table= pd.read_csv('life_expectancy.csv',index_col=0)

bel1980=table.loc['Belgium','1980']

table.plot.scatter('1960','2014')

#years becomes the index 
table2=table.transpose()

be=table

plt.xlabel("Date")
plt.ylabel("Values")
plt.title("Sample Time Series Plot")
pandas.plot()


