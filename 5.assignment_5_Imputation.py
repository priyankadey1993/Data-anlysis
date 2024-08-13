# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 12:59:21 2024

@author: soura
"""

'''
Problem Statement:  
Majority of the datasets have missing values, that might be because the data collected were not at regular intervals or the breakdown of instruments and so on.
 It is nearly impossible to build the proper model or in other words, get accurate results. The common techniques are either removing those records completely or 
 substitute those missing values with the logical ones, there are various techniques to treat these types of problems.
1)	Prepare the dataset using various techniques to solve the problem, explore all the techniques available and use them to see which gives the best result.
            Hint:  Go through this link: https://360digitmg.com/mindmap-data-science


'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#clamates df
cla_df=pd.read_csv(r"C:\Users\soura\Documents\data enginneer\EDA\CLASS 4\Assignments_Datasets\claimants.csv")

from sklearn.impute import SimpleImputer


cla_df.dtypes


cla_df.isna().sum()
'''
CLMSEX       12
CLMINSUR     41
SEATBELT     48
CLMAGE      189
it has null value
'''
#creting three dataframes for climet  in which we store mena ,mediaun ,mode
mean_cla_df=cla_df
median_cla_df=cla_df
mode_cla_df=cla_df

'''CLMSEX'''
# replacing the value with mean
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
mean_cla_df["CLMSEX"] = pd.DataFrame(mean_imputer.fit_transform(mean_cla_df[["CLMSEX"]]))
mean_cla_df["CLMSEX"].isna().sum()

# replacing value with medium
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
median_cla_df["CLMSEX"] = pd.DataFrame(median_imputer.fit_transform(median_cla_df[["CLMSEX"]]))
median_cla_df["CLMSEX"].isna().sum()

# replacing value with mode
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
mode_cla_df["CLMSEX"] = pd.DataFrame(mode_imputer.fit_transform(mode_cla_df[["CLMSEX"]]))
mode_cla_df["CLMSEX"].isna().sum()


#----------------------------------------------------------------------------#
'''CLMINSUR'''
# replacing the value with mean
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
mean_cla_df["CLMINSUR"] = pd.DataFrame(mean_imputer.fit_transform(mean_cla_df[["CLMINSUR"]]))
mean_cla_df["CLMINSUR"].isna().sum()

# replacing value with medium
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
median_cla_df["CLMINSUR"] = pd.DataFrame(median_imputer.fit_transform(median_cla_df[["CLMINSUR"]]))
median_cla_df["CLMINSUR"].isna().sum()

# replacing value with mode
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
mode_cla_df["CLMINSUR"] = pd.DataFrame(mode_imputer.fit_transform(mode_cla_df[["CLMINSUR"]]))
mode_cla_df["CLMINSUR"].isna().sum()

#----------------------------------------------------------------------#
'''SEATBELT'''
# replacing the value with mean
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
mean_cla_df["SEATBELT"] = pd.DataFrame(mean_imputer.fit_transform(mean_cla_df[["SEATBELT"]]))
mean_cla_df["SEATBELT"].isna().sum()

# replacing value with medium
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
median_cla_df["SEATBELT"] = pd.DataFrame(median_imputer.fit_transform(median_cla_df[["SEATBELT"]]))
median_cla_df["SEATBELT"].isna().sum()

# replacing value with mode
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
mode_cla_df["SEATBELT"] = pd.DataFrame(mode_imputer.fit_transform(mode_cla_df[["SEATBELT"]]))
mode_cla_df["SEATBELT"].isna().sum()

#---------------------------------------------------------------#
#----------------------------------------------------------------------#
'''CLMAGE'''
# replacing the value with mean
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
mean_cla_df["CLMAGE"] = pd.DataFrame(mean_imputer.fit_transform(mean_cla_df[["CLMAGE"]]))
mean_cla_df["CLMAGE"].isna().sum()

# replacing value with medium
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
median_cla_df["CLMAGE"] = pd.DataFrame(median_imputer.fit_transform(median_cla_df[["CLMAGE"]]))
median_cla_df["CLMAGE"].isna().sum()

# replacing value with mode
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
mode_cla_df["CLMAGE"] = pd.DataFrame(mode_imputer.fit_transform(mode_cla_df[["CLMAGE"]]))
mode_cla_df["CLMAGE"].isna().sum()



mean_cla_df.isna().sum()
median_cla_df.isna().sum()
mode_cla_df.isna().sum()
