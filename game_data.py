from itertools import count
from platform import platform
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

#select all games and thier publishers with a critic score over 90
data = data[['Publisher','Name', 'Critic_Score']]
data = data.query('Critic_Score >  90')
data['Count'] = data.groupby('Publisher')['Publisher'].transform('count')
data = data.drop_duplicates(subset=['Publisher'])
data = data[['Publisher', 'Count']]
data = data.sort_values(['Count'], ascending = False)
data = data.head(10)
data = data.sort_values(['Count'], ascending = True)
print(data)
data.plot.barh(x='Publisher', y='Count',
             title='Most Sucessful Publishers', color='green')
plt.show()



