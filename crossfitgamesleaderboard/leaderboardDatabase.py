# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd 

"""
CREATE THE LEADERBOARD DATABASE

Stores it in the default directory
"""

class leaderboardDatabase:

    def __init__(self, filePath, databaseName):
        # Create folder to save DB
        if filePath is None:
            raise Exception("No File Path Specified")
        else:
            self.directory = str(filePath) + str(databaseName) + '.db'

    """
    CREATE THE DATABASE AND THE TABLES AND SCHEMA STRUCTURE.
    """
    def createDB(self):
        print(self.directory)
        conn = sqlite3.connect(self.directory)
        conn.execute('''CREATE TABLE leaderboardScores (ordinal INT, rank INT, score INT, scoreDisplay TEXT,
        mobileScoreDisplay TEXT, scoreIdentifier TEXT, scaled INT, video INT, breakdown TEXT, time INT, judge TEXT,
        affiliate TEXT, heat TEXT, lane TEXT, competitorId INT)''')
        conn.execute('''CREATE TABLE leaderboardAthletes (competitorId INT, competitorName TEXT, firstName TEXT, lastName TEXT,
        status TEXT, postCompStatus TEXT, gender TEXT, profilePicS3key TEXT, countryOfOriginCode TEXT, countryOfOriginName TEXT,
        divisionId TEXT, affiliateId INT, affiliateName TEXT, age INT, height TEXT, weight TEXT)''')
        conn.close()

    """
    INSERT THE DATA INTO THE DATABASE
    """
    def insertRows(self, athletes, scores):
        conn = sqlite3.connect(self.directory)

        conn.executemany('''INSERT INTO leaderboardScores(ordinal, rank , score , scoreDisplay ,
        mobileScoreDisplay , scoreIdentifier , scaled , video , breakdown , time , judge ,
        affiliate , heat , lane, competitorId )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', scores)
        conn.commit()
        
        conn.executemany('''INSERT INTO leaderboardAthletes(competitorId , competitorName , firstName , lastName ,
        status , postCompStatus , gender , profilePicS3key , countryOfOriginCode , countryOfOriginName ,
        divisionId , affiliateId , affiliateName , age , height , weight )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', athletes)
        conn.close()
    
    """
    RETURN THE NUMBER OF ROWS IN EACH TABLE
    """
    def checkStatus(self):
        conn = sqlite3.connect(self.directory).cursor()
        conn.execute('SELECT COUNT(*) from leaderboardScores')
        countScores = conn.fetchone()
        conn.execute('SELECT COUNT(*) from leaderboardAthletes')
        countAthletes = conn.fetchone()
        return(countAthletes, countScores)