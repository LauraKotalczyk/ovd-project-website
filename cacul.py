import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st
 
dataset = pd.read_csv("Test_Data.csv", sep=",")

###### step 1: descriptive statistics  #####
##print (dataset.head())

time = dataset['T.T escena (ms)']

print("Variable Time : ")
## Mean
mean = np.mean(time)
print ("Mean : ", round(mean, 2))

## Median
median = np.median(time)
print ("Median : ", round(median, 2))

## Quartille

Q1 = round(np.percentile(time, 25))
print("Quartile Q1 : ", Q1)

Q3 = round(np.percentile(time, 75))
print("Quartile Q3 : ", Q3)

## Variance
variance = np.var(time)
print ("Variance : ", round(variance, 2))

## Standard deviation
Stdeviation = np.std(time)
print ("Standard deviation : ", round(Stdeviation, 2))