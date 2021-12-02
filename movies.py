import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('movieDB.db')
cur = conn.cursor()

table_schema = """
CREATE TABLE IF NOT EXISTS movies (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  MOVIE TEXT NOT NULL,
  LEAD_ACTOR TEXT NOT NULL,
  LEAD_ACTRESS TEXT NOT NULL,
  YEAR INTEGER NOT NULL,
  DIRECTOR TEXT
);
"""
values1 = ('3 Idiots', 'Aamir Khan', 'Kareena Kapoor', 2009, 'Rajkumar Hirani')
values2 = ('Ramleela', 'Ranveer Singh', 'Deepika Padukone', 2013, 'Sanjay Leela Bhansali')
values3 = ('Phantom', 'Saif Ali Khan', 'Katrina Kaif', 2015, 'Kabir Khan')
values4 = ('Rockstar', 'Ranbir Kapoor', 'Nargis Fakhri', 2011, 'Imtiaz Ali')

records = [values1, values2, values3, values4]

cur.execute(table_schema)
cur.execute('SELECT * FROM movies')

result = cur.fetchall()

if not result:
  cur.executemany("INSERT INTO movies (MOVIE, LEAD_ACTOR, LEAD_ACTRESS, YEAR, DIRECTOR) VALUES (?, ?, ?, ?, ?)", records)
  conn.commit()
  cur.execute('SELECT * FROM movies')
  result = cur.fetchall()
  print(tabulate(result, headers=['ID', 'Movie', 'Lead Actor', 'Lead Actress', 'Year', 'Director']))
else:
  print(tabulate(result, headers=['ID', 'Movie', 'Lead Actor', 'Lead Actress', 'Year', 'Director']))

cur.close()
conn.close()
