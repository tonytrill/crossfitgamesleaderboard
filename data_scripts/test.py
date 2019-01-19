import requests
import pandas as pd
import csv
from datetime import date

# ping the CF Games Open leaderboard and store the JSON as csv to be used in analysis

entrants = []
leaderboard_scores = []
failed_pages = []


url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2019/leaderboards?division=1&' \
    'region=0&scaled=0&sort=0&occupation=0&page=1'
response = requests.get(url)
json_output = response.json()

# Pull the total number pages in the API.
for key, value in json_output.items():
    if key == 'pagination':
        totalPages = value['totalPages']
        break
    else:
        continue


for i in range(1, totalPages+1):
    # Attempt to get the JSON data, if not then log that it failed in a list
    try:
        url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2019/leaderboards?division=1&' \
              'region=0&scaled=0&sort=0&occupation=0&page=' + str(i)
        response = requests.get(url)
        json_output = response.json()
        # Athletes is a list of JSON athletes files
        athletes = json_output["leaderboardRows"]
        print(i)
    except:
        print(i, " - failed to process page")
        failed_pages.append(i)
        continue
