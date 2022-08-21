from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the csv file
data = pd.read_csv("video_game.csv")

#clean the data converting str to numbers where needed + drop unwanted columns
data = data.drop(columns=["NA_players", "EU_players", "JP_players", "Other_players", "Global_players", "User_Count", "Rating", "Critic_Count"])


data['User_Score'] = pd.to_numeric(data['User_Score'] ,errors='coerce')
data = data.replace(np.nan, 0, regex=True)
data['User_Score'] = data['User_Score'].astype(float)

data['Critic_Score'] = pd.to_numeric(data['Critic_Score'] ,errors='coerce')
data = data.replace(np.nan, 0, regex=True)
data['Critic_Score'] = data['Critic_Score'].astype(float)

#select all games with a user score over 9 and critic score over 90
results = data[(data['Critic_Score'] >= 90)] 
results1 = results[(data['User_Score'] >= 9)]
results2 = results.count()


print(results2)



