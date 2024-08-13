# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:32:31 2024

@author: soura
"""

import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib as plt
'''
1)	Prepare the dataset by performing the preprocessing techniques, to have all the features in numeric format.

Index	Animals	Gender	Homly	Types
1	Cat	Male	Yes	A
2	Dog	Male	Yes	B
3	Mouse	Male	Yes	C
4	Mouse	Male	Yes	C
5	Dog	Female	Yes	A
6	Cat	Female	Yes	B
7	Lion	Female	Yes	D
8	Goat	Female	Yes	E
9	Cat	Female	Yes	A
10	Dog	Male	Yes	B






'''

dfdummy=pd.read_csv(r"C:\Users\soura\Documents\data enginneer\EDA\CLASS 4\Assignments_Datasets\Animal_category.csv")
dfdummy.dtypes

dummies_ani = pd.get_dummies(dfdummy.Animals)
mergeged_dummy_ani=pd.concat([dfdummy,dummies_ani],axis="columns")
mergeged_dummy_ani
#dummy trap
final_dummi_ani=mergeged_dummy_ani.drop(["Animals","Mouse"],axis="columns")
final_dummi_ani





from sklearn.preprocessing import LabelEncoder
# cppying all data of dfdummy table to dfle
le = LabelEncoder()
df_le=dfdummy
# Assuming 'Homly' is always 'Yes', no need to encode
df_le['Animals'] = le.fit_transform(df_le['Animals'])
df_le['Gender'] = le.fit_transform(df_le['Gender'])
df_le['Types'] = le.fit_transform(df_le['Types'])
df_le.head()
#x=f

'''
report
Name of feature  	description	     type 	revalance
Index               index no	         int 64	no need to change
Animals    	        types of animal 	object	convert it into no using label encoding according to given no 
Gender           	types of gender	object	convert it into no using label encoding according to given no 
Homly      object	types of homely	object	did not did any changes
Types      object	types of types	object	convert it into no using label encoding according to given no 
dtype: object		object	
			
animal	index no		
Cat	      1		
Dog	      2		
Gpat      3		
Lion 	  4		
Mouse	  5		
			
gender			
male	     1		
female	2		
			
Types			
A	     1		
B	     2		
C	     3		
D	     4		













'''












'''
from sklearn.linear_model import LinearRegression
model=LinearRegression()

#Consider as a type as result 
x=final_dummi_ani.drop("Types",axis=1)
x # showing all comun apart of TYpes colum
y=final_dummi_ani.Types
y# showing only type column
model.fit(x,y)
'''

