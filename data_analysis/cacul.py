import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm
from statsmodels.formula.api import ols

dataset300 = pd.read_csv("Scene_300.csv", sep=",")
dataset301 = pd.read_csv("Scene_301.csv", sep=",")

## Merge dataset
df_Final = pd.merge(dataset300, dataset301, on='User')
print(df_Final.head())
df_Final=df_Final[['User','favoriteColor_x','yearOfBirth_x','country_x','easyNav_x','colorblind_x','device_x','userID_x','easyRead_x','avgNumberOPurchases_x','appealingColor_x','gender_x','T. scene time (ms)_x','Nº error cliks_x','T. scene time (ms)_y','Nº error cliks_y']]
## Cacul new columns
df_Final["TimeTotal"]=df_Final['T. scene time (ms)_y']+df_Final['T. scene time (ms)_x']
df_Final["ClickTotal"]=df_Final['Nº error cliks_y']+df_Final['Nº error cliks_x']
df_Final['colorComb'] = np.where(df_Final['userID_x']== 2,'blue', 'yellow')

###### step 1: descriptive statistics  #####
##print (dataset.head())

print("Summary Statistics for the time needed (in ms): ")

## N = Number of Participants
print("Number of answers :",len(df_Final))

## Number of valid data
## delete test entrie
df_Final = df_Final.loc[df_Final['User'] !='OPK92648699060616889872231497102023']
## delete colorblind
colorblind=(df_Final['colorblind_x']=="yes").sum()
print("Number of colorblind : ",colorblind)

df_Final = df_Final.loc[df_Final['colorblind_x'] !='yes']
## delete  time 

time = df_Final["TimeTotal"]

Q1 = round(np.percentile(time, 25))
Q3 = round(np.percentile(time, 75))

QR=Q3-Q1
lowerLimit=Q1-1.5*QR
upperLimit=Q3+1.5*QR
print("upper limit for time",upperLimit)
df_Final = df_Final.loc[df_Final["TimeTotal"] < upperLimit]

print("Number of answers after cleanning : ",len(df_Final))
## Global statistic

print("-----Global desciption-----")

df_Final['age'] = 2023-df_Final['yearOfBirth_x']
mean = np.mean(df_Final['age'])
print ("Mean of age : ", round(mean, 2))

## Plot
def label_function(val):
    return f'\n{val:.0f}%'

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(16, 8))

df_Final.groupby('country_x').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 20},
                                  ax=ax1)
df_Final.groupby('gender_x').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 20},
                                  ax=ax2)
df_Final.groupby('device_x').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 20},
                                  ax=ax3)
ax1.set_ylabel('Country', size=22)
ax2.set_ylabel('Gender', size=22)
ax3.set_ylabel('Device', size=22)
plt.tight_layout()
plt.show()


mean = np.mean(df_Final["ClickTotal"])
print ("Mean of error click: ", round(mean, 2))

mean = np.mean(df_Final['easyNav_x'])
print ("Mean of easy navigation : ", round(mean, 2))

mean = np.mean(df_Final["easyRead_x"])
print ("Mean of easy read ", round(mean, 2))

mean = np.mean(df_Final["appealingColor_x"])
print ("Mean of appealing color: ", round(mean, 2))



## statistic about time 
print("-- Statistique about Time --")
time = df_Final["TimeTotal"]

## Mean
mean = np.mean(time)
print ("%s%d%s" % ("Mean : ", round(mean, 2), " ms"))

mean = np.mean(df_Final["TimeTotal"])
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
blue = df_Final[(df_Final.colorComb == 'blue')]
print("Number of answers :",len(blue))

mean = np.mean(blue['age'])
print ("Mean of age : ", round(mean, 2))

nbmen=(blue['gender_x']=="male").sum()
print("Number of men :",nbmen )
nbwom=(blue['gender_x']=="female").sum()
print("Number of women :",nbwom )

print(blue.groupby(['country_x'])['country_x'].count())

print(blue.groupby(['device_x'])['device_x'].count())

##colorblind=(blue['colorblind']=="yes").sum()
##print("Number of colorblind : ",colorblind )

mean = np.mean(blue["TimeTotal"])
print ("Mean of time : ", round(mean, 2))

mean = np.mean(blue["ClickTotal"])
print ("Mean of error click: ", round(mean, 2))

mean = np.mean(blue['easyNav_x'])
print ("Mean of easy navigation : ", round(mean, 2))

mean = np.mean(blue["easyRead_x"])
print ("Mean of easy read ", round(mean, 2))

mean = np.mean(blue["appealingColor_x"])
print ("Mean of appealing color: ", round(mean, 2))

print("----- YELLOW -------")
yellow = df_Final[(df_Final.colorComb == 'yellow')]
print("Number of answers :",len(yellow))

mean = np.mean(yellow['age'])
print ("Mean of age : ", round(mean, 2))

nbmen=(yellow['gender_x']=="male").sum()
print("Number of men :",nbmen )
nbwom=(yellow['gender_x']=="female").sum()
print("Number of women :",nbwom )

print(yellow.groupby(['country_x'])['country_x'].count())

print(yellow.groupby(['device_x'])['device_x'].count())

##colorblind=(yellow['colorblind']=="yes").sum()
##print("Number of colorblind : ",colorblind )

mean = np.mean(yellow["TimeTotal"])
print ("Mean of time : ", round(mean, 2))

mean = np.mean(yellow["ClickTotal"])
print ("Mean of error click: ", round(mean, 2))

mean = np.mean(yellow['easyNav_x'])
print ("Mean of easy navigation : ", round(mean, 2))

mean = np.mean(yellow["easyRead_x"])
print ("Mean of easy read ", round(mean, 2))

mean = np.mean(yellow["appealingColor_x"])
print ("Mean of appealing color: ", round(mean, 2))

## T Test
print("----- T Test ------")
print("----- Time ------")
X1 = blue["TimeTotal"]
X2 = yellow["TimeTotal"]

y = st.ttest_ind(X1,X2) 
print(" P value :",y[1])
print( "if p value <  0.05 -> significative difference")

print("----- Eror click ------")
X1 = blue["ClickTotal"]
X2 = yellow["ClickTotal"]

y = st.ttest_ind(X1,X2) 
print(" P value :",y[1])
print( "if p value <  0.05 -> significative difference")


print("----- Easy Navigation ------")
X1 = blue['easyNav_x']
X2 = yellow['easyNav_x']

y = st.ttest_ind(X1,X2) 
print(" P value :",y[1])
print( "if p value <  0.05 -> significative difference")

print("----- Easy Read ------")
X1 = blue['easyRead_x']
X2 = yellow['easyRead_x']

y = st.ttest_ind(X1,X2) 
print(" P value :",y[1])
print( "if p value <  0.05 -> significative difference")

print("----- Appealing Color ------")
X1 = blue['appealingColor_x']
X2 = yellow['appealingColor_x']

y = st.ttest_ind(X1,X2) 
print(" P value :",y[1])
print( "if p value <  0.05 -> significative difference")

## anova test
print("----- ANOVA TEST ------")

print("--- Color Combinaison / Gender")
model = ols('TimeTotal ~ C(colorComb) + C(gender_x) + C(colorComb):C(gender_x)', data=df_Final).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("P-value: ", anova_table.iloc[2,3])
print( "if p value <  0.05 -> significative difference")

print("--- Color Combinaison / Age")
model = ols('TimeTotal ~ C(colorComb) + C(age) + C(colorComb):C(age)', data=df_Final).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("P-value: ", anova_table.iloc[2,3])
print( "if p value <  0.05 -> significative difference")

print("--- Color Combinaison / Country")
model = ols('TimeTotal ~ C(colorComb) + C(country_x) + C(colorComb):C(country_x)', data=df_Final).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("P-value: ", anova_table.iloc[2,3])
print( "if p value <  0.05 -> significative difference")

print("--- Color Combinaison / Device")
model = ols('TimeTotal ~ C(colorComb) + C(device_x) + C(colorComb):C(device_x)', data=df_Final).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("P-value: ", anova_table.iloc[2,3])
print( "if p value <  0.05 -> significative difference")





#plot