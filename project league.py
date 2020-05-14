# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importing libraries
import pandas as pd
import numpy as np
import requests
import re
import json 
from pandas.io.json import json_normalize #special package in pandas
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from random import randint

#importing our dataset
df = pd.read_csv("/Users/Lana/Downloads/league_team_data.csv")
#There are 31278 rows with 25 columns that comrpise this DataFrame

#data type of each column (variable) of the dataframe
df.dtypes
# 15 int64 (integer), 1 float64 (float), 6 bool (boolean), and 3 object (String)

df.size
#there are 781950 elements that comrprise the dataframe

#looking for any potentail missing values 
df.isnull().sum()
#There are no missing values

#looking for any duplicated 
duplicateRowsdf = df[df.duplicated()]
print("Duplicate Rows except for first occurrence based on all columns are: ")
print(duplicateRowsdf)
#There are no duplicates! 


############# Descriptive Stats for categorical variables ##############
df['win'].value_counts()
#15639 wins, 15639 fails 


df['gameVersion'].value_counts()
df['gameVersion'].mode()
#central tendancy is gameVersion 10.7.314.9802 
########################################################################

######## Descriptive Statistics of numeric variables #########
df['gameDuration(seconds)'].describe()
#the average game duration is 1473.72 seconds (24.56 minutes)
#minimum duration of a gatch is 432.18 seconds (7.20 minutes)
#maximum duration of a game is 3766 seconds (62.77 minutes)

df['towerKills'].describe()
#average total team tower kills in a match is 4.49
#minimum team tower kills: 0
#maximum team tower kills: 11

df['inhibitorKills'].describe()
#average team inhibitor kills in a match is 0.76
#minimum: 0
#maximum: 11

df['baronKills'].describe()
#average team baron kills in a match is 0.32
#minimum: 0
#maximum: 5

df['dragonKills'].describe()
#average team dragon kills in a match is 1.41
#minimum: 0
#maximum: 9

df['riftHeraldKills'].describe()
#average team rift herald kills is 0.58
#minimum: 0
#maximm: 2

df['teamKills'].describe()
#average number of particiapnt kills in a match is 27.95
#minimum: 0
#maximum: 98

df['teamDeaths'].describe()
#average number of particiapnt deaths in a match is 28.05
#minimum: 0
#maximum: 99

df['teamAssists'].describe()
#average number of particiapnt assists in a match is 48.05 
#minimum: 0
#maximum: 247

df['teamTotalDamageDealtToChampions'].describe()
#average number of particiapnt damage dealt to champions in a match is 79389.74 
#minimum: 352
#maximum: 432178

df['teamVisionScore'].describe()
#the average participant vision score is 104.51
#minimum: 0
#maximum: 419

df['teamGoldEarned'].describe()
#the average amount of gold earned by participant is 51467.36
#minimum:3764
#maximum: 177717

df['teamAverageChampLevel'].describe()
#the average participant champ level is 13.76
#minimum: 1.20
#maximum: 22.60

df['teamTotalMinionsKilled'].describe()
#the average number of minions killed by participant is 486.44
#minimum: 0
#maximum: 1244

#######################################################################3

################ Boxplots #####################
#ploting a boxplot for outliers for gameDuration
df.boxplot(column=['gameDuration(seconds)'])

#ploting a boxplot for outliers for towerKills
df.boxplot(column=['towerKills'])

#boxplot for outliers for inhibitorKills
df.boxplot(column=['inhibitorKills'])

#boxplot for outlier for baronKills
df.boxplot(column=['baronKills'])

#boxplot for outlier for dragonKills
df.boxplot(column=['dragonKills'])

#boxplot for outlier for riftHeraldKills
df.boxplot(column=['riftHeraldKills'])

#boxplot for outlier for kills
df.boxplot(column=['teamKills'])

#boxplot for outlier for deaths
df.boxplot(column=['teamDeaths'])

#boxplot for outlier for assists
df.boxplot(column=['teamAssists'])

#boxplot for outlier for totalDamageDealtToChampions
df.boxplot(column=['teamTotalDamageDealtToChampions'])

#boxplot for outlier for visionScore
df.boxplot(column=['teamVisionScore'])

#boxplot for outlier for goldEarned
df.boxplot(column=['teamGoldEarned'])

#boxplot for outlier for averageChampLevel
df.boxplot(column=['teamAverageChampLevel'])

#boxplot for outlier for totalMinionsKilled
df.boxplot(column=['teamMinionsKilled'])

######################################################################


###### Subsetting #######

###### creating a subset where teams won the match ######
win = df.loc[df['win'] == 'Win']
win['team'].value_counts()
#red team won 8123 matches and blue team won 7516 matches

win['firstBlood'].value_counts()
#9200 obtained firstBlood and won, 6439 did and still won

win['firstTower'].value_counts()
#11084 obtained firstTower and won, 4555 didnt and still won

win['firstInhibitor'].value_counts()
#11312 obtained firstInhibitor and won, 4327 didnt and still won

win['firstBaron'].value_counts()
#6264 obtained first baron and won, 9375 didnt and still won

win['firstDragon'].value_counts()
#8312 obtaine firstDragon and won, 7327 didnt and still won

win['firstRiftHerald'].value_counts()
#8265 obtain firstRiftHerald and won, 7374 didnt and still won

###### creating a subset where teams lost the match ######
lost = df.loc[df['win'] == 'Fail']
lost['team'].value_counts()
#Blue lost 8123, Red lost 7516

lost['firstBlood'].value_counts()
#9226 teams did not obtain firstBlood and lost
#6414 teams did and still lost

lost['firstTower'].value_counts()
#11190 teams did not obtain firstBlood and lost
#4449 did and still lost

lost['firstInhibitor'].value_counts()
#14329 teams did not obtain firstInhibitor and lost
#1310 did and still lost

lost['firstBaron'].value_counts()
#14248 teams did not obtain firstBaron and lost
#1391 teams did and still lost

lost['firstDragon'].value_counts()
#11109 teams did not obtain firstDragon and lost
#4530 teams did and still lost

lost['firstRiftHerald'].value_counts()
#11109 teams did not obtain firstDragon and lost
#4320 teams did and still lost


###### subset of red team winning ######

red_win = win.loc[win['team'] == 'Red']
red_lost = lost.loc[lost['team'] == 'Red']

###### subset of blue team winning ######
blue_win = win.loc[win['team'] == 'Blue']
blue_lost = lost.loc[lost['team'] == 'Blue']


#######################################################################
### used to create PQ tables 2 and 3 in Project Step 2
red_win['firstBlood'].value_counts()
red_win['firstTower'].value_counts()
red_win['firstInhibitor'].value_counts()
red_win['firstBaron'].value_counts()
red_win['firstDragon'].value_counts()
red_win['firstRiftHerald'].value_counts()

red_lost['firstBlood'].value_counts()
red_lost['firstTower'].value_counts()
red_lost['firstInhibitor'].value_counts()
red_lost['firstBaron'].value_counts()
red_lost['firstDragon'].value_counts()
red_lost['firstRiftHerald'].value_counts()


blue_win['firstBlood'].value_counts()
blue_win['firstTower'].value_counts()
blue_win['firstInhibitor'].value_counts()
blue_win['firstBaron'].value_counts()
blue_win['firstDragon'].value_counts()
blue_win['firstRiftHerald'].value_counts()

blue_lost['firstBlood'].value_counts()
blue_lost['firstTower'].value_counts()
blue_lost['firstInhibitor'].value_counts()
blue_lost['firstBaron'].value_counts()
blue_lost['firstDragon'].value_counts()
blue_lost['firstRiftHerald'].value_counts()

############### Visualizations ######################

## this shit is being played with ###
import matplotlib.pyplot as plt
#visualizing a histogram for goldEarned for winning and losing match
##maybe???????######
a = win["teamGoldEarned"]
b = lost["teamGoldEarned"]
plt.hist([a, b], label=['a', 'b'])
plt.legend(loc='upper right')
plt.show()

########### boxplots of boolean variables with win subset #################

plot_var = win['firstBaron'].value_counts().plot(kind='bar')
plot_var.set_xlabel("Achieved First Baron")
plot_var.set_ylabel("Number of Team Wins")
plot_var.set_title("Number of Team Wins vs Achievement of First Baron ")

plot_var = win['firstBlood'].value_counts().plot(kind='bar')
plot_var.set_xlabel("Achieved First Blood")
plot_var.set_ylabel("Number of Team Wins")
plot_var.set_title("Number of Team Wins vs Achievement of First Blood ")

plot_var = win['firstTower'].value_counts().plot(kind='bar')
plot_var.set_xlabel("Achieved First Tower")
plot_var.set_ylabel("Number of Team Wins")
plot_var.set_title("Number of Team Wins vs Achievement of First Tower ")

plot_var = win['firstInhibitor'].value_counts().plot(kind='bar')
plot_var.set_xlabel("Achieved First Inhibitor")
plot_var.set_ylabel("Number of Team Wins")
plot_var.set_title("Number of Team Wins vs Achievement of First Inhibitor ")

plot_var = win['firstBaron'].value_counts().plot(kind='bar')
plot_var.set_xlabel("Achieved First Baron")
plot_var.set_ylabel("Number of Team Wins")
plot_var.set_title("Number of Team Wins vs Achievement of First Baron")

plot_var = win['firstDragon'].value_counts().plot(kind='bar')
plot_var.set_xlabel("Achieved First Dragon")
plot_var.set_ylabel("Number of Team Wins")
plot_var.set_title("Number of Team Wins vs Achievement of First Dragon")

plot_var = win['firstRiftHerald'].value_counts().plot(kind='bar')
plot_var.set_xlabel("Achieved First Rift Herald")
plot_var.set_ylabel("Number of Team Wins")
plot_var.set_title("Number of Team Wins vs Achievement of First Rift Herald")

 