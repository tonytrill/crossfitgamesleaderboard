"""
Tony Silva
CrossFit Games Open 2019 API Data Project
"""

import requests
import pandas as pd
import csv
from datetime import date

# ping the CF Games Open leaderboard and store the JSON as csv to be used in analysis

entrants = []
leaderboard_scores = []
failed_pages = []


url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2017/leaderboards?division=1&' \
    'region=0&scaled=0&sort=0&occupation=0&page=1'
response = requests.get(url)
json_output = response.json()

# Pull the total number pages in the API so we know how many pages we should iterate through
for key, value in json_output.items():
    if key == 'totalpages':
        totalPages = value


for i in range(1, totalPages+1):
    # Attempt to get the JSON data, if not then log that it failed in a list
    try:
        url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2017/leaderboards?division=1&region=0&scaled=0&sort=0&occupation=0&page=' + str(
            i)
        response = requests.get(url)
        json_output = response.json()
        # Athletes is a list of JSON athletes files
        athletes = json_output["athletes"]
        print(i)
    except:
        print(i, " - failed to process page")
        failed_pages.append(i)
        continue

    for athlete in athletes:
        #scores = athlete["scores"]
        entrant = {"userid": athlete["userid"], "name": athlete["name"]}
        entrants.append(entrant)

entrants_csv = pd.DataFrame(entrants)
#scores_csv = pd.DataFrame(leaderboard_scores)

today = str(date.today())
entrants_csv.to_csv('~/Data/athletes_men_2017_'+today+'.csv', index=False)
#scores_csv.to_csv('~/Data/scores_men_2017_'+today+'.csv', index=False)

# with open('~/Data/failed_pages_women.csv', 'w') as myfile:
#     wr = csv.writer(myfile, lineterminator='\n')
#     for page in failed_pages:
#         wr.writerow([page])
