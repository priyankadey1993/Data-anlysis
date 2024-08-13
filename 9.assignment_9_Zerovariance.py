# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:43:59 2024

@author: Priyanka dey

"""

'''

Variance measures how far a set of data is spread out. A variance of zero indicates that all the data values are identical. There are various techniques to remove this for transforming the data into the suitable one for prediction.
Problem statement: 
Find which columns of the given dataset with zero variance, and explore various techniques used to remove the zero variance from the dataset to perform certain analysis. 

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\soura\Documents\data enginneer\EDA\CLASS 4\Assignments_Datasets\Z_dataset.csv")
df.dtypes
numeric_columns = df.select_dtypes(include=np.number)

# Calculating the variance of each numeric variable in the DataFrame
numeric_columns.var()

# Checking if the variance of each numeric variable is equal to 0 and returning a boolean Series
numeric_columns.var() == 0 

# Checking if the variance of each numeric variable along axis 0 (columns) is equal to 0 and returning a boolean Series
numeric_columns.var(axis=0) == 0
zero_variance_columns= numeric_columns.var(axis=0).index.tolist()

df_cleaned = df.drop(columns=zero_variance_columns)



