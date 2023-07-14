import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st
 
dataset = pd.read_csv("Test_Data.csv", sep=",")

###### step 1: descriptive statistics  #####
##print (dataset.head())

time = dataset['T.T escena (ms)']
print("Number of answers :",len(time))

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

## Plot
plt.hist(x=time, bins='auto', color='#0504aa')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('Experience time per person')
plt.show()

print("----- BLUE -------")
blue = dataset[(dataset.userID == 2)]
print("Number of answers :",len(blue))

blue['age'] = 2023-blue['yearOfBirth']
mean = np.mean(blue['age'])
print ("Mean of age : ", round(mean, 2))

nbmen=(blue['gender']=="male").sum()
print("Number of men :",nbmen )
nbwom=(blue['gender']=="female").sum()
print("Number of women :",nbwom )

print(blue.groupby(['country']).size())

print("----- YELLOW -------")
yellow = dataset[(dataset.userID == 1)]
print("Number of answers :",len(yellow))

yellow['age'] = 2023-yellow['yearOfBirth']
mean = np.mean(yellow['age'])
print ("Mean of age : ", round(mean, 2))

nbmen=(yellow['gender']=="male").sum()
print("Number of men :",nbmen )
nbwom=(yellow['gender']=="female").sum()
print("Number of women :",nbwom )