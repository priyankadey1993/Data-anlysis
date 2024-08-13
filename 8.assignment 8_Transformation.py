# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:18:23 2024

@author: soura
"""

# Normal Quantile-Quantile Plot

# Importing pandas library for data manipulation
import pandas as pd

# Reading data from a CSV file named "education.csv" located at "C:/Data/"
data = pd.read_csv(r"C:\Users\soura\Documents\data enginneer\EDA\CLASS 4\Assignments_Datasets\calories_consumed.csv")
data.dtypes

import scipy.stats as stats
# Importing pylab module for creating plots
import pylab

stats.probplot(data["Weight gained (grams)"], dist="norm", plot=pylab)
stats.probplot(data["Calories Consumed"],dist="norm",plot=pylab)

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
plt.hist(data["Weight gained (grams)"])
plt.show()
data['log_values_weight'] = np.log(data['Weight gained (grams)'])
plt.hist(data["log_values_weight"])

stats.probplot(data["log_values_weight"], dist=stats.norm, plot=pylab)
stats.probplot(data["Weight gained (grams)"], dist=stats.norm, plot=pylab)

from feature_engine import transformation

# Set up the Yeo-Johnson transformer for 'workex' variable
tf = transformation.YeoJohnsonTransformer(variables='Weight gained (grams)')

# Transforming the 'workex' variable using Yeo-Johnson transformation
data_tf = tf.fit_transform(data)

# Transformed data
# Checking whether the transformed 'workex' data is normally distributed using a Q-Q plot
prob = stats.probplot(data_tf["Weight gained (grams)"], dist=stats.norm, plot=pylab)



'''
fitted_data, fitted_lambda = stats.boxcox(data["Weight gained (grams)"])
fig, ax = plt.subplots(1, 2)
sns.distplot(data["Weight gained (grams)"], hist=False, kde=True,
             kde_kws={'shade': True, 'linewidth': 2},
             label="Non-Normal", color="green", ax=ax[0])

sns.distplot(fitted_data, hist=False, kde=True,
             kde_kws={'shade': True, 'linewidth': 2},
             label="Normal", color="green", ax=ax[1])
'''