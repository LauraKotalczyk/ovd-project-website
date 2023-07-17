import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st
 
dataset = pd.read_csv("data_analysis/Final_Data.csv", sep=",")

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