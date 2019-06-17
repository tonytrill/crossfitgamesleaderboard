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
            self.directory = '~/' + str(databaseName) + '.db'
        else:
            self.directory = str(filePath) + str(databaseName) + '.db'

    """
    CREATE THE DATABASE AND THE TABLES AND SCHEMA STRUCTURE.
    """
    def createDB(self):
        print(self.directory)
        conn = sqlite3.connect(self.directory)
        conn.execute('''CREATE TABLE leaderboardScores ()''')
        conn.execute('''CREATE TABLE leaderboardAthletes ()''')
        conn.close()

    """
    INSERT THE DATA INTO THE DATABASE
    """
    def insertRows(self):
        conn = sqlite3.connect(self.directory)
        # conn = append athletes
        # conn = append scores
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

test = leaderboardDatabase(None, 'test')
test.createDB()