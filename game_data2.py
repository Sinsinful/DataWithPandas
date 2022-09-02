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

#filter all the NES games released in 1988 on the list
df2 = df.loc[(df['Platform'] == 'NES') & (df['Year_of_Release'] == 1988)]

score = [94, 78, 80, 76, 72, 43, 94, 95, 65, 35, 68]

#add new column and populate with the review scores from the list score

df2['Review_Score'] = score
df2.Review_Score = pd.to_numeric(df2.Review_Score, errors='coerce')
df2.sort_values('Review_Score', ascending=True, inplace=True)

#create barchart
df2.plot.barh(x='Name', y='Review_Score',
             title='NES Games Released In 1988', color='royalblue')
plt.xlabel('Average review score of game')
plt.show()

