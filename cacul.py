import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st
 
dataset = pd.read_csv("Test_Data.csv", sep=",")

print (dataset.head())