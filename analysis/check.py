
import sqlite3

conn = sqlite3.connect('/Users/silv6928/test.db')
cursor = conn.cursor()
cursor.execute('''select * from leaderboardAthletes; ''')
print(cursor.fetchall())
conn.close()