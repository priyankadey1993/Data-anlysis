# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:22:44 2024

@author: soura
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
'''
Data is one of the most important assets. Often the data are stored in distinct systems with different formats and scales.
 These seemingly small differences in how the data is stored can result in misinterpretations and inconsistencies in your analytics.
 Inconsistency can make it impossible to deliver reliable information to management for good decision-making. We have the preprocessing 
 techniques to make the data uniform. 

1)	Prepare the dataset by performing the preprocessing techniques, to have the standard scale to data.

'''

data = pd.read_csv(r"C:\Users\soura\Documents\data enginneer\EDA\CLASS 4\Assignments_Datasets\Seeds_data.csv")
data.dtypes
# checking null value
data.isna().sum()
#checking duplicate value
data.duplicated().sum()
# copy the data new old data so the previous version is store
data_old=data
# checking the outlier
sns.boxplot(data.Compactness)
sns.boxplot(data.Assymetry_coeff)
# in two colum outlier detcted so craeten f new df and winsoraixation technique is use
#

from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['Compactness'])

new_data = winsor.fit_transform(data[['Compactness']])
sns.boxplot(new_data.Compactness)

data['Compactness']= new_data.Compactness
# removed the outlier from comoactness column

sns.boxplot(data.Compactness)

winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['Assymetry_coeff'])

new_data = winsor.fit_transform(data[['Assymetry_coeff']])
sns.boxplot(new_data.Assymetry_coeff)

data['Assymetry_coeff']= new_data.Assymetry_coeff
sns.boxplot(data.Assymetry_coeff)
data.dtypes

#remove the outliser from asummertic column

#so the reportnow
print(data.dtypes)

# Check for missing values
print(data.isnull().sum())

# Check for duplicates
print(data.duplicated().sum())

# Describe numerical data
print(data.describe())

# checking the scaling
from sklearn.preprocessing import StandardScaler
a = data.describe()
print (a)
# Initialise the Scaler
scaler = StandardScaler()

# To scale data
data_std= scaler.fit_transform(data)
print(data_std)
# Convert the array back to a dataframe
dataset = pd.DataFrame(data_std)
res = dataset.describe()
print(res)

# min max scaling

from sklearn.preprocessing import MinMaxScaler
# Min-Max Scaling
scaler = MinMaxScaler()
data_min_max = scaler.fit_transform(data)
print (data_min_max)
data_set_min_max=pd.DataFrame(data_min_max)
data_set_min_max.describe()