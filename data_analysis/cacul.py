import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st
 
dataset = pd.read_csv("Test_Data.csv", sep=",")

###### step 1: descriptive statistics  #####
##print (dataset.head())

print("Summary Statistics for the time needed (in ms): ")

## N = Number of Participants
time = dataset['T.T escena (ms)']
print("Number of answers :",len(time))


## Mean
mean = np.mean(time)
print ("%s%d%s" % ("Mean : ", round(mean, 2), " ms"))

## Median
median = np.median(time)
print ("%s%d%s" % ("Median : ", round(median, 2), " ms"))

## Quartille

Q1 = round(np.percentile(time, 25))
print ("%s%d%s" % ("Q1 Quartile : ", Q1, " ms"))


Q3 = round(np.percentile(time, 75))
print ("%s%d%s" % ("Q3 Quartile : ", Q3, " ms"))


## Variance
variance = np.var(time)
print ("%s%d%s" % ("Variance : ", round(variance, 2), " ms"))


## Standard deviation
stdDeviation = np.std(time)
print ("%s%d%s" % ("Standard deviation : ", round(stdDeviation, 2), " ms"))


## Plot
plt.hist(x=time, bins='auto', color='#0504aa')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('Experience time per person')

plt.savefig("fig.pdf")

plt.show()

## Statistic by color group 
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

print(blue.groupby(['device']).size())

colorblind=(blue['colorblind']=="yes").sum()
print("Number of colorblind : ",colorblind )

mean = np.mean(blue['T.T escena (ms)'])
print ("Mean of time : ", round(mean, 2))

mean = np.mean(blue['Nº clicks erróneos'])
print ("Mean of error click: ", round(mean, 2))

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

print(yellow.groupby(['country']).size())

print(yellow.groupby(['device']).size())

colorblind=(yellow['colorblind']=="yes").sum()
print("Number of colorblind : ",colorblind )

mean = np.mean(yellow['T.T escena (ms)'])
print ("Mean of time : ", round(mean, 2))

mean = np.mean(yellow['Nº clicks erróneos'])
print ("Mean of error click: ", round(mean, 2))
