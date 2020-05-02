# -*- coding: utf-8 -*-
import pandas as pd
import csv
from datetime import date
import requests

"""
'https://games.crossfit.com/competitions/api/v1/competitions/open/2019/leaderboards?division=1&' \
    'region=0&scaled=0&sort=0&occupation=0&page=1'
"""

def getJSON(url):
        response = requests.get(url)
        json_output = response.json()
        return json_output

def convertDict(listofdicts):
    list_to_pass = []
    for singleDict in listofdicts:
        list_to_pass.append(tuple(singleDict.values()))
    return(list_to_pass)


"""
A CF GAMES API URL CLASS

Creates API calls to the 2019 CROSSFIT GAMES Leaderboard
Able to query different leaderboard as well.
"""
# Get the 2019 CROSSFIT GAMES URL
class gamesURL:
    
    base_url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2019/leaderboards'
    
    def __init__(self, division, region, scaled, occupation, page):
        self.division=division
        self.region = region
        self.scaled = scaled
        self.occupation = occupation
        self.page = page
        self.url = str(self.base_url + '&division=' +str(self.division) + '&region=' + str(self.region) + '&scaled=' + str(self.scaled) + '&occupation=' + str(self.occupation) +'&page=' + str(self.page))

    """
    Increase the page number for pagination
    """
    def incrementPage(self):
        self.page = self.page + 1

    """
    Return the page number  (helper)
    """
    def returnPage(self):
        return (self.page)
    
    """
    Change the page number to an exact integer
    """
    def setPage(self, n):
        self.page = int(n)

    """
    Returns the total number of pages for the given URL based on User's query
    Used for pagination
    """
    def getTotalPages(self):
        request = getJSON(self.url)
        totalPages = request['pagination']
        totalPages = totalPages['totalPages']
        return (totalPages)

    """
    PARSES THE SINGLE JSON RESPONSE IT GETS BACK FROM THE CF API
    """
    def parseJSON(self):
        request = getJSON(self.url)
        leader_board_rows = request['leaderboardRows']
        athletes = []
        leaderboard_scores = []
        for row in leader_board_rows:
            athlete = row['entrant']
            athletes.append(athlete)
            scores = row['scores']
            for score in scores:
                # Need the competitorId to tie scores back to athletes
                score["competitorId"] = str(athlete["competitorId"])
                score["ordinal"] = str(score["ordinal"])
                score['ordinal'] = '' if 'ordinal' not in score else score['ordinal']
                score['rank'] = '' if 'rank' not in score else score['rank']
                score['score'] = '' if 'score' not in score else score['score']
                score['scoreDisplay'] = '' if 'scoreDisplay' not in score else score['scoreDisplay'] 
                score['mobileScoreDisplay'] = '' if 'mobileScoreDisplay' not in score else score['mobileScoreDisplay']
                score['scoreIdentifier'] = '' if 'scoreIdentifier' not in score else score['scoreIdentifier']
                score['scaled'] = '' if 'scaled' not in score else score['scaled']
                score['video'] = '' if 'video' not in score else score['video']
                score['breakdown'] = '' if 'breakdown' not in score else score['breakdown']
                score['time'] = '' if 'time' not in score else score['time']
                score['judge'] = '' if 'judge' not in score else score['judge']
                score['affiliate'] = '' if 'affiliate' not in score else score['affiliate']
                score['heat'] = '' if 'heat' not in score else score['heat']
                score['lane'] = '' if 'lane' not in score else score['lane']
                
                leaderboard_scores.append(score)
        del(row, score, athlete)
        leaderboard_scores = convertDict(leaderboard_scores)
        athletes = convertDict(athletes)
        return(athletes, leaderboard_scores)

    """
    LOOP THROUGH ALL OF THE PAGES FOR THE URL GIVEN ON THE LEADERBOARD AND PUT THE CONTENTS INTO A MASTER LIST
    """
    def extractAllData(self):
        total_athletes = []
        total_scores = []
        for i in range(self.getTotalPages()):
            athletes, scores = self.parseJSON()
            total_athletes = total_athletes + athletes
            total_scores = total_scores + scores
            self.incrementPage()
            print(i)
        #self.saveData(total_athletes, total_scores)
        self.setPage(1) # Reset the page number if object is reused.
        return(total_athletes, total_scores)
        

#test = gamesURL(1,0,0,0,1)

#print(test.parseJSON()[1])