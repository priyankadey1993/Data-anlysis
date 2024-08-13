# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:36:21 2024

@author: Priyanka Dey
"""

'''
Q1. For the given dataset perform the type casting (convert the datatypes, ex. float to int)
Q2. Check for duplicate values, and handle the duplicate values (ex. drop)
Q3. Do the data analysis (EDA)?
Such as histogram, boxplot, scatterplot, etc.

'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#online retail data frame
'''
inline retail .csv has a issue in csv file so anble to upload that why
upload mtcars.csv. please check the data from mt cars.csv
'''
On_re_df=pd.read_csv(r"C:\Users\soura\Documents\data enginneer\EDA\Data preprocesing\InClass Data Sets\InClass_DataPreprocessing_datasets\mtcars_dup.csv")
On_re_df.dtypes

# convert the data type float to int
On_re_df["mpg"]= On_re_df["mpg"].astype(int)
On_re_df["disp"]= On_re_df["disp"].astype(int)
On_re_df["drat"]= On_re_df["drat"].astype(int)
On_re_df["wt"]= On_re_df["wt"].astype(int)
On_re_df["qsec"]= On_re_df["qsec"].astype(int)

On_re_df.dtypes

#Q2. Check for duplicate values, and handle the duplicate values (ex. drop)
duplicate = On_re_df.duplicated()  # Returns Boolean Series denoting duplicate rows.
On_re_df.duplicated().sum()
On_re_df.drop_duplicates(keep="first",inplace=True)
On_re_df.duplicated().sum()

On_re_df.isna().sum()
#checking hsitogram of the data frame
plt.hist(On_re_df.mpg)
plt.hist(On_re_df.cyl)
plt.hist(On_re_df.disp)
plt.hist(On_re_df.hp)
plt.hist(On_re_df.drat)
plt.hist(On_re_df.wt)
plt.hist(On_re_df.qsec)
plt.hist(On_re_df.vs)
plt.hist(On_re_df.am)
plt.hist(On_re_df.gear)
plt.hist(On_re_df.carb)

# chcking outlier

sns.boxplot(On_re_df.mpg)
#outlier detected

sns.boxplot(On_re_df.cyl)
#no outlier

sns.boxplot(On_re_df.disp)
#no outlier

sns.boxplot(On_re_df.hp)
#outlier detect

sns.boxplot(On_re_df.drat)
# not requred

sns.boxplot(On_re_df.wt)
#outlier detected

sns.boxplot(On_re_df.qsec)
#outlier detced

sns.boxplot(On_re_df.vs)
#no outlier
sns.boxplot(On_re_df.am)
#no outlier

sns.boxplot(On_re_df.gear)
#no outlier
sns.boxplot(On_re_df.carb)
#no outlier

# outlier removing
from feature_engine.outliers import Winsorizer
def outlier_remove_function(df, column_name):
    
    winsor_iqr = Winsorizer(capping_method='iqr', 
                            tail='right', 
                            fold=1.5, 
                            variables=[column_name])

     # Fitting the Winsorizer model to the 'Salaries' column and transforming the data
    df_new  = winsor_iqr.fit_transform(On_re_df[[column_name]])
    df_new .head()
    return df_new

    
df_new=outlier_remove_function(On_re_df,"mpg")
On_re_df["mpg"]=df_new["mpg"]
sns.boxplot(On_re_df.mpg)

df_new=outlier_remove_function(On_re_df,"hp")
On_re_df["hp"]=df_new["hp"]
sns.boxplot(On_re_df.hp)

df_new=outlier_remove_function(On_re_df,"wt")
On_re_df["wt"]=df_new["wt"]
sns.boxplot(On_re_df.wt)


def outlier_remove_function_left(df, column_name):
    
    winsor_iqr = Winsorizer(capping_method='iqr', 
                            tail='left', 
                            fold=1.5, 
                            variables=[column_name])

     # Fitting the Winsorizer model to the 'Salaries' column and transforming the data
    df_new  = winsor_iqr.fit_transform(On_re_df[[column_name]])
    df_new .head()
    return df_new


df_new=outlier_remove_function(On_re_df,"qsec")
On_re_df["qsec"]=df_new["qsec"]
sns.boxplot(On_re_df.qsec)

df_new=outlier_remove_function_left(On_re_df,"qsec")
On_re_df["qsec"]=df_new["qsec"]
sns.boxplot(On_re_df.qsec)

corr_matrix = On_re_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

sns.pairplot(On_re_df)
plt.show()
# scattered plot
sns.scatterplot(x='mpg', y='cyl', data=On_re_df)
plt.show()

sns.scatterplot(x='disp', y='hp', data=On_re_df)
plt.show()

sns.scatterplot(x='drat', y='wt', data=On_re_df)
plt.show()

sns.scatterplot(x='qsec', y='vs', data=On_re_df)
plt.show()

sns.scatterplot(x='am', y='gear', data=On_re_df)
plt.show()