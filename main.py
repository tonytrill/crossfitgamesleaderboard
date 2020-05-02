# -*- coding: utf-8 -*-
from crossfitgamesleaderboard import url
from crossfitgamesleaderboard import leaderboardDatabase
import sys

def main():
    test = leaderboardDatabase.leaderboardDatabase()
    try:
        test.createDB()
    except:
        print("Database already created with that name!")
    men = url.gamesURL(1,0,0,0,1)
    #women = url.gamesURL(2,0,0,0,1)
    men_athletes, men_scores = men.parseJSON()
    #women.extractAllData()
    print(men_scores)
    test.insertRows(men_athletes, men_scores)

    print(test.checkStatus())

if __name__ == "__main__":
    main()