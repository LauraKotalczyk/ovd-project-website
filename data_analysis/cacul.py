import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st

dataset = pd.read_csv("Final_Data.csv", sep=",")

###### step 1: descriptive statistics  #####
##print (dataset.head())

print("Summary Statistics for the time needed (in ms): ")

## N = Number of Participants
time = dataset['T. scene time (ms)']
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

print(blue.groupby(['country'])['country'].count())

print(blue.groupby(['device'])['device'].count())

colorblind=(blue['colorblind']=="yes").sum()
print("Number of colorblind : ",colorblind )

mean = np.mean(blue['T. scene time (ms)'])
print ("Mean of time : ", round(mean, 2))

mean = np.mean(blue['Nº error cliks'])
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

print(yellow.groupby(['country'])['country'].count())

print(yellow.groupby(['device'])['device'].count())

colorblind=(yellow['colorblind']=="yes").sum()
print("Number of colorblind : ",colorblind )

mean = np.mean(yellow['T. scene time (ms)'])
print ("Mean of time : ", round(mean, 2))

mean = np.mean(yellow['Nº error cliks'])
print ("Mean of error click: ", round(mean, 2))

## T Test
print("----- T Test ------")
print("----- Time ------")
X1 = blue['T. scene time (ms)']
X2 = yellow['T. scene time (ms)']

y = st.ttest_ind(X1,X2) 
print(" P value :",y[1])
print( "if p value <  0.05 -> significative difference")

print("----- Eror click ------")
X1 = blue['Nº error cliks']
X2 = yellow['Nº error cliks']

y = st.ttest_ind(X1,X2) 
print(" P value :",y[1])
print( "if p value <  0.05 -> significative difference")