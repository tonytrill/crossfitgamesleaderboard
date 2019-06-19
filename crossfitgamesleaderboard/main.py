# -*- coding: utf-8 -*-
import url
import leaderboardDatabase
import sys

def main(file_path):
    test = leaderboardDatabase.leaderboardDatabase(file_path, 'test')
    try:
        test.createDB()
    except:
        print("Database already created with that name!")
    men = url.gamesURL(1,0,0,0,1)
    women = url.gamesURL(2,0,0,0,1)
    men_athletes, men_scores = men.parseJSON()
    #women.extractAllData()

    test.insertRows(men_athletes, men_scores)

    print(men_athletes)

if __name__ == "__main__":
    main('/Users/silv6928/')