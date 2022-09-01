from itertools import count
from platform import platform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the csv file
df = pd.read_csv("video_game.csv")

#clean the data converting str to numbers where needed + drop unwanted columns
df = df.drop(columns=["NA_players", "EU_players", "JP_players", "Other_players", "Global_players", "User_Count", "Rating", "Critic_Count"])


df['User_Score'] = pd.to_numeric(df['User_Score'] ,errors='coerce')
df = df.replace(np.nan, 0, regex=True)
df['User_Score'] = df['User_Score'].astype(float)

df['Critic_Score'] = pd.to_numeric(df['Critic_Score'] ,errors='coerce')
df = df.replace(np.nan, 0, regex=True)
df['Critic_Score'] = df['Critic_Score'].astype(float)

"""
#usefull pandas functions

#print top 3 rows
print(df.head(3))

#print bottom 3 rows
print(df.tail(3))

#read headers
print(df.columns)

#read specific column, top 5
print(df['Name'] [0:5])

#read multiple columns, top 5
print(df[['Name', 'Platform']] [0:5])

#read each rows
print(df.iloc[1:4])

#read a specicic location
print(df.iloc[2,1])

#iterate through rows
for index, row in df.iterrows():
    print(index, row)

#iterate through rows returning a specific column item
for index, row in df.iterrows():
    print(index, row['Name'])

#filter a specific item in a specific column
print(df.loc[df['Platform'] == 'NES'])

#sort values by a value
print(df.sort_values('Name', ascending=False))

#add new column with data from other rows combined and manipulated
df['Total'] = df['Critic_Score'] + df['User_Score'] * 10
print(df.head(3))


#filter data with multiple conditions *note pandas uses | & insted of or and
print(df.loc[(df['Platform'] == 'NES') & (df['Year_of_Release'] == 1988)])
"""