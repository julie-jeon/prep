import datetime as dt
from re import I
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Milestone Action Items
# Download the data set about Value of Energy Cost Saving Program for businesses in New York City (under the "Export" option, there is a way to retrieve a CSV file). Answer the following questions.

# How many different companies are represented in the data set?
# What is the total number of jobs created for businesses in Queens?
# How many different unique email domains names are there in the data set?
# Considering only NTAs with at least 5 listed businesses, what is the average total savings and the total jobs created for each NTA?
# Save your result for the previous question as a CSV file.v

def read_data():
    data = pd.read_csv('Value_of_Energy_Cost_Savings_Program_Savings_for_Businesses_-_FY2020.csv')
    return data

data = read_data()
print(data)