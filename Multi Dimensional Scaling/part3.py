# This script scrapes data from NFL.com for each of the 32 teams in the NFL and writes the data out to
# two .csv files.
from bs4 import BeautifulSoup
import urllib2
import time
import csv

# dictionary linking each team in the NFL with its 3-letter acronym.
team_names = {'ARI': 'Arizona Cardinals',
'ATL': 'Atlanta Falcons',
'BAL': 'Baltimore Ravens',
'BUF': 'Buffalo Bills',
'CAR': 'Carolina Panthers',
'CHI': 'Chicago Bears',
'CIN': 'Cincinnati Bengals',
'CLE': 'Cleveland Browns',
'DAL': 'Dallas Cowboys',
'DEN': 'Denver Broncos',
'DET': 'Detroit Lions',
'GB': 'Green Bay Packers',
'HOU': 'Houston Texans',
'IND': 'Indianapolis Colts',
'JAX': 'Jacksonville Jaguars',
'KC': 'Kansas City Chiefs',
'MIA': 'Miami Dolphins',
'MIN': 'Minnesota Vikings',
'NE': 'New England Patriots',
'NO': 'New Orleans Saints',
'NYG': 'New York Giants',
'NYJ': 'New York Jets',
'OAK': 'Oakland Raiders',
'PHI': 'Philadelphia Eagles',
'PIT': 'Pittsburgh Steelers',
'SD': 'San Diego Chargers',
'SEA': 'Seattle Seahawks',
'SF': 'San Francisco 49ers',
'STL': 'Saint Louis Rams',
'TB': 'Tampa Bay Buccaneers',
'TEN': 'Tennessee Titans',
'WAS': 'Washington Redskins'}

# lists and dictionaries associated with the data storage
all_team_stats = {}
all_team_stats_list = []
all_team_statso = {}
all_team_statso_list = []

# iterating through each NFL team
for i in range(0, len(team_names)):
    url = 'http://www.nfl.com/teams/statistics?season=2015&team=' + team_names.keys()[i] + '&seasonType=REG'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), 'html.parser') # package used to read HTML content of website

    team_stats = {}
    team_stats_list = []
    table = soup.find("table", {"class": 'data-table1 team-stats'})
    rows = table.find_all("tr")
    for j in range(2, 18):
        row_sections = rows[j].find_all("td")
        if j == 3:
            team_stats['1st Downs Rush'] = row_sections[1].get_text().split("-")[0].strip()
            team_stats['1st Downs Pass'] = row_sections[1].get_text().split("-")[1].strip()
            team_stats['1st Downs By Penalty'] = row_sections[1].get_text().split("-")[2].strip()
        elif j == 7:
            team_stats['Offense Plays'] = row_sections[1].get_text().split("-")[0].strip()
            team_stats['Offense Avg Yds'] = row_sections[1].get_text().split("-")[1].strip()
        elif j == 9:
            team_stats['Rushing Plays'] = row_sections[1].get_text().split("-")[0].strip()
            team_stats['Rushing Avg Yds'] = row_sections[1].get_text().split("-")[1].strip()
        elif j == 11:
            team_stats['Passing Completions'] = row_sections[1].get_text().split("-")[0].strip()
            team_stats['Passing Attepmts'] = row_sections[1].get_text().split("-")[1].strip()
            team_stats['Passing Interceptions'] = row_sections[1].get_text().split("-")[2].strip()
            team_stats['Passing Average'] = row_sections[1].get_text().split("-")[3].strip()
        elif j == 15:
            team_stats['Rushing Touchdowns'] = row_sections[1].get_text().split("-")[0].strip()
            team_stats['Passing Touchdowns'] = row_sections[1].get_text().split("-")[1].strip()
            team_stats['Return Touchdowns'] = row_sections[1].get_text().split("-")[2].strip()
            team_stats['Defensive Touchdowns'] = row_sections[1].get_text().split("-")[3].strip()
        elif j == 16:
            team_stats['Time of Possession'] = row_sections[1].get_text().split(':')[0] + '.' + str(float(row_sections[1].get_text().split(':')[1])/60.0).split('.')[1]
        else:
            team_stats[row_sections[0].get_text()] = row_sections[1].get_text()

    # storing the scraped data into the associated lists and dictionaries
    all_team_stats[team_names.keys()[i]] = team_stats
    time.sleep(1)
    team_stats_list.append(team_names.keys()[i])
    for i in range(0, len(team_stats)):
        team_stats_list.append(team_stats[sorted(team_stats)[i]])
    all_team_stats_list.append(team_stats_list)

for i in range(0, len(team_names)):
    url = 'http://www.nfl.com/teams/statistics?season=2015&team=' + team_names.keys()[i] + '&seasonType=REG'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), 'html.parser')
    # sum_touchdowns = 0
    # for key, value in all_team_stats.items():
    #     sum_touchdowns += int(value['Touchdowns'])
    # print sum_touchdowns
    team_statso = {}
    team_statso_list = []
    table = soup.find("table", {"class": 'data-table1 team-stats'})
    rows = table.find_all("tr")
    for j in range(2, 18):
        row_sections = rows[j].find_all("td")
        if j == 3:
            team_statso['1st Downs Rush'] = row_sections[2].get_text().split("-")[0].strip()
            team_statso['1st Downs Pass'] = row_sections[2].get_text().split("-")[1].strip()
            team_statso['1st Downs By Penalty'] = row_sections[2].get_text().split("-")[2].strip()
        elif j == 7:
            team_statso['Offense Plays'] = row_sections[2].get_text().split("-")[0].strip()
            team_statso['Offense Avg Yds'] = row_sections[2].get_text().split("-")[1].strip()
        elif j == 9:
            team_statso['Rushing Plays'] = row_sections[2].get_text().split("-")[0].strip()
            team_statso['Rushing Avg Yds'] = row_sections[2].get_text().split("-")[1].strip()
        elif j == 11:
            team_statso['Passing Completions'] = row_sections[2].get_text().split("-")[0].strip()
            team_statso['Passing Attepmts'] = row_sections[2].get_text().split("-")[1].strip()
            team_statso['Passing Interceptions'] = row_sections[2].get_text().split("-")[2].strip()
            team_statso['Passing Average'] = row_sections[2].get_text().split("-")[3].strip()
        elif j == 15:
            team_statso['Rushing Touchdowns'] = row_sections[2].get_text().split("-")[0].strip()
            team_statso['Passing Touchdowns'] = row_sections[2].get_text().split("-")[1].strip()
            team_statso['Return Touchdowns'] = row_sections[2].get_text().split("-")[2].strip()
            team_statso['Defensive Touchdowns'] = row_sections[2].get_text().split("-")[3].strip()
        elif j == 16:
            team_statso['Time of Possession'] = row_sections[2].get_text().split(':')[0] + '.' + str(float(row_sections[2].get_text().split(':')[1])/60.0).split('.')[1]
        else:
            try:
                team_statso[row_sections[0].get_text()] = row_sections[2].get_text()
            except:
                team_statso[row_sections[0].get_text()] = 'NONE'
    # storing the scraped data into the associated lists and dictionaries
    all_team_statso[team_names.keys()[i]] = team_statso
    time.sleep(1)
    team_statso_list.append(team_names.keys()[i])
    for i in range(0, len(team_statso)):
        team_statso_list.append(team_statso[sorted(team_statso)[i]])
    all_team_statso_list.append(team_statso_list)

# writing the data obtained to a .csv file
with open('nfl_team_stats2015.csv', 'wb') as csvfile:
    data_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['Team', '1st Downs By Penalty', '1st Downs Pass', '1st Downs Rush', '3rd Down Conversions', '4th Down Conversions', 'Defensive Touchdowns',
       'Field Goals',  'Offense Avg Yds', 'Offense Plays', 'Passing Attepmts','Passing Average', 'Passing Completions',
       'Passing Interceptions', 'Passing Touchdowns', 'Return Touchdowns', 'Rushing Avg Yds', 'Rushing Plays', 'Rushing Touchdowns',
       'Sacks','Time of Possession', 'Total First Downs', 'Total Offensive Yds', 'Total Passing Yds', 'Total Rushing Yds', 'Touchdowns',
       'Turnover Ratio'])
    for team_stats_list in all_team_stats_list:
        data_writer.writerow(team_stats_list)
    csvfile.close()

with open('nfl_team_stats2015o.csv', 'wb') as csvfile:
    data_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['Team', '1st Downs By Penalty', '1st Downs Pass', '1st Downs Rush', '3rd Down Conversions', '4th Down Conversions', 'Defensive Touchdowns',
       'Field Goals',  'Offense Avg Yds', 'Offense Plays', 'Passing Attepmts','Passing Average', 'Passing Completions',
       'Passing Interceptions', 'Passing Touchdowns', 'Return Touchdowns', 'Rushing Avg Yds', 'Rushing Plays', 'Rushing Touchdowns',
       'Sacks','Time of Possession', 'Total First Downs', 'Total Offensive Yds', 'Total Passing Yds', 'Total Rushing Yds', 'Touchdowns',
       'Turnover Ratio'])
    for team_statso_list in all_team_statso_list:
        data_writer.writerow(team_statso_list)
    csvfile.close()