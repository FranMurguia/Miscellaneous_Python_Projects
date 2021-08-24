# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:36:12 2021

@author: FranJa
"""
import pandas as pd
import matplotlib as plt

# # Remove all rows with NULL values

# df = pd.read_csv('data_1.csv')

# remove_df = df.dropna()

# print(remove_df.to_string())



# # Replace empty values for specified columns

# df = pd.read_csv('data_1.csv')

# df["Calories"].fillna(130, inplace=True)

# print(df.to_string())



# # Calculate the MEAN, MEDIAN or MODE and replace any empty values with it

# df = pd.read_csv('data_1.csv')

# calories_mean = df["Calories"].mean()
# calories_median = df["Calories"].median()
# calories_mode = df["Calories"].mode()[0]

# print("Mean: ", calories_mean, "\n")
# print("Median: ", calories_median, "\n")
# print("Mode: ", calories_mode, "\n")

# df["Calories"].fillna(calories_mode , inplace = True)
# print(df.to_string())



# # Convert into a correct format

# df = pd.read_csv('data_1.csv')

# df['Date'] = pd.to_datetime(df['Date'])

# print ( df.to_string() ,'\n')

# df.dropna(subset=['Date'], inplace = True)

# print ( df.to_string() , "\n")



# # Replace a value (only for small data sets)

# df = pd.read_csv('data_1.csv')

# df.loc[7,'Duration'] = 45

# print ( df.to_string() ,'\n')



# # Replace wrong values with a loop

# df = pd.read_csv('data_1.csv')

# for value in df.index:
#     if df.loc[value, "Duration"] > 120:
#         df.loc[value, "Duration"] = 120

# print ( df.to_string() ,'\n')



# # Removing rows

# df = pd.read_csv("data_1.csv")

# for value in df.index:
#     if df.loc[value, "Duration"] > 120:
#         df.drop(index = value, inplace=True)

# print( df.to_string() , "\n")



# # Duplicates values

# df = pd.read_csv("data_1.csv")

# print(df.duplicated())

# df.drop_duplicates(inplace=True)

# print(df.to_string())



# # Correlation

# df = pd.read_csv("data_2.csv")

# print(df.corr())



# Plotting

df = pd.read_csv("data_2.csv")

# # Scatter plot

# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

# Histogram

df["Duration"].plot(kind = 'hist')




