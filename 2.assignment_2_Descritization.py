# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:28:33 2024

@author: soura
"""
'''
1)	Convert the continuous data into discrete classes on the iris dataset.
Prepare the dataset by performing the preprocessing techniques, to have the data which improves model performance.
Sepal.Length	Sepal.Width	Petal.Length	Petal.Width	Species
5.1	3.5	1.4	0.2	setosa
4.9	3	1.4	0.2	setosa
4.7	3.2	1.3	0.2	setosa
4.6	3.1	1.5	0.2	setosa
5	3.6	1.4	0.2	setosa
5.4	3.9	1.7	0.4	setosa
4.6	3.4	1.4	0.3	setosa
5	3.4	1.5	0.2	setosa
4.4	2.9	1.4	0.2	setosa
4.9	3.1	1.5	0.1	setosa

'''
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib as plt
dfpt=pd.read_csv(r"C:\Users\soura\Documents\data enginneer\EDA\CLASS 4\Assignments_Datasets\iris.csv")
dfpt.dtypes

#decritization
#creating discrtizartion for dfpt["Sepal.Length"] 
dfpt["Sepal.Length"].max()
dfpt["Sepal.Length"].min()
#creating discrtizartion for dfpt["Sepal.Length"] column name sepal_len_cat
dfpt["sepal.length_cat"]=pd.cut(x=dfpt["Sepal.Length"],bins=[dfpt["Sepal.Length"].min(),dfpt["Sepal.Length"].quantile(0.25),dfpt["Sepal.Length"].median(),dfpt["Sepal.Length"].quantile(0.75),dfpt["Sepal.Length"].max()],
                               labels = ["poor","belowe avg","avg","good" ])
import matplotlib.pyplot as plt

def draw_barplot(xbar):
    s=xbar.value_counts()
    plt.title("catatgorical plot of sepal_length")
    plt.xlabel("catagorry of length")
    plt.ylabel("frequency of length")   
    plt.bar(s.index,s.values)
    return 
draw_barplot(dfpt["sepal.length_cat"])
# barplot of dfpt["sepal.length_cat"] 

#-----------------------------------------------------------------------------------------------------------------#
#creating discrtizartion for dfpt["Sepal.Width"] 
dfpt["Sepal.Width"].max()
dfpt["Sepal.Width"].min()
dfpt["sepal.Width_cat"]=pd.cut(x=dfpt["Sepal.Width"],bins=[dfpt["Sepal.Width"].min(),dfpt["Sepal.Width"].quantile(0.25),dfpt["Sepal.Width"].median(),dfpt["Sepal.Width"].quantile(0.75),dfpt["Sepal.Width"].max()],
                               labels = ["poor","belowe avg","avg","good" ])
#barplot
import matplotlib.pyplot as plt

def draw_barplot(xbar):
    s=xbar.value_counts()
    plt.title("catatgorical plot of sepal_width")
    plt.xlabel("catagorry of width")
    plt.ylabel("frequency of width")
    plt.bar(s.index,s.values)
    return 
draw_barplot(dfpt["sepal.Width_cat"])

#-------------------------------------------------------------------------#
#creating discrtizartion for dfpt["Petal.Length"] 
dfpt.dtypes
dfpt["Petal.Length"].max()
dfpt["Petal.Length"].min()
dfpt["Petal.Length_cat"]=pd.cut(x=dfpt["Petal.Length"],bins=[dfpt["Petal.Length"].min(),dfpt["Petal.Length"].quantile(0.25),dfpt["Petal.Length"].median(),dfpt["Petal.Length"].quantile(0.75),dfpt["Petal.Length"].max()],
                               labels = ["poor","belowe avg","avg","good" ])
#barplot
import matplotlib.pyplot as plt

def draw_barplot(xbar):
    s=xbar.value_counts()
    plt.title("catatgorical plot of petal_length")
    plt.xlabel("catagorry of length")
    plt.ylabel("frequency of length")
    plt.bar(s.index,s.values)
    return 
draw_barplot(dfpt["Petal.Length_cat"])

#-------------------------------------------------------------------------------------#
#creating discrtizartion for dfpt["Petal.Width"] 
dfpt["Petal.Width"].max()
dfpt["Petal.Width"].min()
dfpt["Petal.Width_cat"]=pd.cut(x=dfpt["Petal.Width"],bins=[dfpt["Petal.Width"].min(),dfpt["Petal.Width"].quantile(0.25),dfpt["Petal.Width"].median(),dfpt["Petal.Width"].quantile(0.75),dfpt["Petal.Width"].max()],
                               labels = ["poor","belowe avg","avg","good" ])
#barplot
import matplotlib.pyplot as plt

def draw_barplot(xbar):
    s=xbar.value_counts()
    plt.title("catatgorical plot of petal_Width")
    plt.xlabel("catagorry of Width")
    plt.ylabel("frequency of Width")
    plt.bar(s.index,s.values)
    return 
draw_barplot(dfpt["Petal.Width_cat"])
#---------------------------------------------------------------------------------#
#creating discrtizartion for dfpt["Unnamed"] 
dfpt["Unnamed: 0"].max()
dfpt["Unnamed: 0"].min()
dfpt["Unnamed_cat"]=pd.cut(x=dfpt["Unnamed: 0"],bins=[dfpt["Unnamed: 0"].min(),dfpt["Unnamed: 0"].quantile(0.25),dfpt["Unnamed: 0"].median(),dfpt["Unnamed: 0"].quantile(0.75),dfpt["Unnamed: 0"].max()],
                               labels = ["poor","belowe avg","avg","good" ])
#barplot
import matplotlib.pyplot as plt

def draw_barplot(xbar):
    s=xbar.value_counts()
    plt.title("catatgorical plot of Unnamed")
    plt.xlabel("catagorry of Unnamed")
    plt.ylabel("frequency of Unnamed")
    plt.bar(s.index,s.values)
    return 
draw_barplot(dfpt["Unnamed_cat"])
#--------------------------------------------------------------------------------------------#

'''
report
Name of feature	description	type	revalance
Unnamed: 0        int64	Created new_colum unnmaed _cat	              int64	              created new_column_Unamed_colum and creted barplot
Sepal.Length    float64	float type craeted new colum sepal_lenth_cat	 float 64	          created new_column_sepal_length_colum and creted barplot
Sepal.Width     float64	Created new_colum Sepal.Width_cat	        float 64              created new_column_sepal_width_colum and creted barplot
Petal.Length    float64	Created new_colum Petal.Length   _cat	    float 64	              created new_column_petal_length_colum and creted barplot
Petal.Width     float64	Created new_colum Petal.Width  _cat	       float 64	              created new_column_petal_width_colum and creted barplot
Species          object			

'''