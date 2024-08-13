# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:28:27 2024

@author: soura
"""

import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib as plt
'''
1.	Prepare the dataset by performing the preprocessing techniques, to treat the outliers.

crim       float64	conatin outlier
zn         float64	contain outlier
indus      float64	not conatin outlier
chas       float64	not conatin outlier
nox        float64	not conatin outlier
rm         float64	contain outlier
age        float64	not conatin outlier
dis        float64	contain outlier
rad        float64	not conatin outlier
tax        float64	not conatin outlier
ptratio    float64	not conatin outlier
black      float64	contain outlier
lstat   float64	not conatin outlier
medv       float64	contain outlier



'''


dfot=pd.read_csv(r"C:\Users\soura\Documents\data enginneer\EDA\CLASS 4\Assignments_Datasets\Boston.csv")
dfot.dtypes
# solving outlier for Crimm
sns.boxplot(dfot.crim)

#finding the upper and lower limit
q1=dfot.crim.quantile(0.25)
q3=dfot.crim.quantile(0.75)
iqr=q3-q1
up_li=q3+(1.5*iqr)
lo_li=q1-(1.5*iqr)
#trim the data
new_df=dfot.loc[(dfot.crim<up_li) &( dfot.crim>lo_li)]

print("new_df",len(new_df))
print("old_df",len(dfot))
print("difference",len(new_df)-len(dfot))
sns.boxplot(new_df.crim)

#changing outlier with lower and upper
new_dfot=dfot
new_dfot.loc[(dfot.crim>up_li,"crim")]=up_li 
new_dfot.loc[(dfot.crim<lo_li,"crim")]=lo_li 

print("new_df",len(new_dfot))
print("old_df",len(dfot))
print("difference",len(new_dfot)-len(dfot))
sns.boxplot(new_dfot.crim)

dfot=new_dfot
#--------------------------------------rm---------------------------------------------------------------
# rm colum conatin outlier
sns.boxplot(dfot.rm)

#finding the upper and lower limit
q1=dfot.rm.quantile(0.25)
q3=dfot.rm.quantile(0.75)
iqr=q3-q1
up_li=q3+(1.5*iqr)
lo_li=q1-(1.5*iqr)
#trim the data
new_df_rm=dfot.loc[(dfot.crim<up_li) &( dfot.crim>lo_li)]

print("new_df_rm",len(new_df_rm))
print("old_df",len(dfot))
print("difference",len(new_df_rm)-len(dfot))
sns.boxplot(new_df_rm.crim)

#changing outlier with lower and upper
new_dfot_rm=dfot
new_dfot_rm.loc[(dfot.rm>up_li,"rm")]=up_li 
new_dfot_rm.loc[(dfot.rm<lo_li,"rm")]=lo_li 

print("new_df",len(new_dfot_rm))
print("old_df",len(dfot))
print("difference",len(new_dfot_rm)-len(dfot))
sns.boxplot(new_dfot_rm.rm)
dfot=new_dfot_rm
#-------------------------------Zn-----------------------------------------------
sns.boxplot(dfot.zn)
q1=dfot.zn.quantile(0.25)
q3=dfot.zn.quantile(0.75)
iqr=q3-q1
up_li=q3+(1.5*iqr)
lo_li=q1-(1.5*iqr)
#trim the data
new_df_zn=dfot.loc[(dfot.zn<up_li) &( dfot.zn>lo_li)]

print("new_df_zn",len(new_df_zn))
print("old_df",len(dfot))
print("difference",len(new_df_zn)-len(dfot))
sns.boxplot(new_df_zn.crim)

#changing outlier with lower and upper
new_dfot_zn=dfot
new_dfot_zn.loc[(dfot.zn>up_li,"zn")]=up_li 
new_dfot_zn.loc[(dfot.zn<lo_li,"zn")]=lo_li 

print("new_df",len(new_dfot_zn))
print("old_df",len(dfot))
print("difference",len(new_dfot_zn)-len(dfot))
sns.boxplot(new_dfot_zn.zn)
dfot=new_dfot_zn
#--------------------dis----------------
sns.boxplot(dfot.dis  )
q1=dfot.dis.quantile(0.25)
q3=dfot.dis.quantile(0.75)
iqr=q3-q1
up_li=q3+(1.5*iqr)
lo_li=q1-(1.5*iqr)
#trim the data
new_df_dis=dfot.loc[(dfot.dis<up_li) &( dfot.dis>lo_li)]

print("new_df_rad",len(new_df_dis))
print("old_df",len(dfot))
print("difference",len(new_df_dis)-len(dfot))
sns.boxplot(new_df_zn.dis)

#changing outlier with lower and upper
new_dfot_dis=dfot
new_dfot_dis.loc[(dfot.dis>up_li,"dis")]=up_li 
new_dfot_dis.loc[(dfot.dis<lo_li,"dis")]=lo_li 

print("new_df",len(new_dfot_dis))
print("old_df",len(dfot))
print("difference",len(new_dfot_dis)-len(dfot))
sns.boxplot(new_dfot_dis.dis)
dfot=new_dfot_dis


#-------black---------------------
sns.boxplot(dfot.black  )
q1=dfot.black.quantile(0.25)
q3=dfot.black.quantile(0.75)
iqr=q3-q1
up_li=q3+(1.5*iqr)
lo_li=q1-(1.5*iqr)
#trim the data
new_df_black=dfot.loc[(dfot.black<up_li) &( dfot.black>lo_li)]

print("new_df_rad",len(new_df_black))
print("old_df",len(dfot))
print("difference",len(new_df_black)-len(dfot))
sns.boxplot(new_df_black.black)

#changing outlier with lower and upper
new_dfot_black=dfot
new_dfot_black.loc[(dfot.black>up_li,"black")]=up_li 
new_dfot_black.loc[(dfot.black<lo_li,"black")]=lo_li 

print("new_df",len(new_dfot_black))
print("old_df",len(dfot))
print("difference",len(new_dfot_black)-len(dfot))
sns.boxplot(new_dfot_black.black)
dfot=new_dfot_black


#-------medv---------------------
sns.boxplot(dfot.medv    )
q1=dfot.medv.quantile(0.25)
q3=dfot.medv.quantile(0.75)
iqr=q3-q1
up_li=q3+(1.5*iqr)
lo_li=q1-(1.5*iqr)
#trim the data
new_df_medv=dfot.loc[(dfot.medv<up_li) &( dfot.medv>lo_li)]

print("new_df_rad",len(new_df_medv))
print("old_df",len(dfot))
print("difference",len(new_df_medv)-len(dfot))
sns.boxplot(new_df_medv.medv)

#changing outlier with lower and upper
new_dfot_medv=dfot
new_dfot_medv.loc[(dfot.medv>up_li,"medv")]=up_li 
new_dfot_medv.loc[(dfot.medv<lo_li,"medv")]=lo_li 

print("new_df",len(new_dfot_medv))
print("old_df",len(dfot))
print("difference",len(new_dfot_medv)-len(dfot))
sns.boxplot(new_dfot_medv.medv)
dfot=new_dfot_medv