# we used Python 2.7.9 and the calculations for the MDS visualizations took around 10 seconds for
# each set of statistics

# this script takes in statistics involved with NFL teams and returns a 2D plot of
# the 32 teams in the NFL

import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold # package used for MDS implementation
import math

# configuration to print entire np arrays
np.set_printoptions(threshold=np.nan)

# reading in .csv data
reader = csv.reader(open("nfl_team_stats2015.csv", "r"), delimiter=';')
readero = csv.reader(open("nfl_team_stats2015o.csv", "r"), delimiter=';')
data = list(reader)
datao = list(readero)

dists = []
teams = []

################################################################################################################
column_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
row_stats = ['Team', '1st Downs By Penalty', '1st Downs Pass', '1st Downs Rush', '3rd Down Conversions', '4th Down Conversions', 'Defensive Touchdowns',
       'Field Goals',  'Offense Avg Yds', 'Offense Plays', 'Passing Attepmts','Passing Average', 'Passing Completions',
       'Passing Interceptions', 'Passing Touchdowns', 'Return Touchdowns', 'Rushing Avg Yds', 'Rushing Plays', 'Rushing Touchdowns',
       'Sacks','Time of Possession', 'Total First Downs', 'Total Offensive Yds', 'Total Passing Yds', 'Total Rushing Yds', 'Touchdowns',
       'Turnover Ratio']

nfl_teams = ['JAX', 'MIN', 'MIA', 'CAR', 'ATL', 'TB', 'DET', 'CIN', 'NYJ', 'HOU', 'GB', 'DEN', 'BAL', 'WAS', 'NYG', 'OAK', 'KC', 'PHI', 'TEN', 'NO', 'DAL', 'PIT', 'NE', 'CLE', 'STL', 'SEA', 'CHI', 'IND', 'ARI', 'BUF', 'SF', 'SD', 'AVERAGE', 'SD']

# this method takes as input a list of different statistics and returns the indices
# of those statistics as they are found in the .csv data file
def stats_to_columns(stats):
    cols = []
    for stat in stats:
        index = row_stats.index(stat)
        cols.append(index)
    return cols

# these statistics are the ones involved in offensive performance
stats_of_interest = ['1st Downs Pass', '1st Downs Rush', 'Offense Avg Yds', 'Offense Plays', 'Passing Average', 'Passing Completions',
         'Passing Touchdowns', 'Rushing Avg Yds', 'Rushing Plays', 'Rushing Touchdowns', 'Total First Downs',
         'Total Offensive Yds', 'Total Passing Yds', 'Total Rushing Yds', 'Touchdowns', 'Time of Possession']

# stats_of_interest = ['Sacks', 'Defensive Touchdowns', 'Passing Interceptions']
# stats_of_interest_defense = []

# these statistics are the ones involved in defensive performance
stats_of_interest_defense = ['1st Downs Pass', '1st Downs Rush', 'Offense Avg Yds', 'Offense Plays', 'Passing Average', 'Passing Completions',
       'Passing Touchdowns', 'Rushing Avg Yds', 'Rushing Plays', 'Rushing Touchdowns', 'Total First Downs',
       'Total Offensive Yds', 'Total Passing Yds', 'Total Rushing Yds', 'Touchdowns']

# this function calculates the distance between two teams given a certain list of offensive and defensive
# statistics
def cost(team1, team2, stats_interested, stats_interested_defense):
    cost_value = 0
    cols = stats_to_columns(stats_interested)
    cols_def = stats_to_columns(stats_interested_defense)
    for i in range(0, len(cols)):
        cost_value = cost_value + math.fabs(((float(data[team1][0].split(',')[cols[i]]) - float(data[33][0].split(',')[cols[i]]))/float(data[34][0].split(',')[cols[i]])) -
                    (float(data[team2][0].split(',')[cols[i]]) - float(data[33][0].split(',')[cols[i]]))/float(data[34][0].split(',')[cols[i]]))
    for i in range(0, len(cols_def)):
        cost_value = cost_value + math.fabs(((float(datao[team1][0].split(',')[cols_def[i]]) - float(datao[33][0].split(',')[cols_def[i]]))/float(datao[34][0].split(',')[cols_def[i]])) -
                    (float(datao[team2][0].split(',')[cols_def[i]]) - float(datao[33][0].split(',')[cols_def[i]]))/float(datao[34][0].split(',')[cols_def[i]]))
    return cost_value

# this portion of code uses the cost function defined above to calculate the distances
# between each pair of teams in the 32 team NFL league
for i in range(1, len(data) - 2):
    dist_team = []
    teams.append(data[i][0].split(',')[0])
    for j in range(1, len(data) - 2):
        dist_team.append(cost(j, i, stats_of_interest, stats_of_interest_defense))
    dists.append(dist_team)
