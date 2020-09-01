import sqlite3

connection = sqlite3.connect('resources/database/database.db')
cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
sessions(
    name varchar(80),
    surname varchar(80),
    session varchar(161)
)"""

cursor.execute(command1)