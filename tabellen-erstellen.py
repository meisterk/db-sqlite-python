import sqlite3
connection = sqlite3.connect('schule.db')
cursur = connection.cursor()

# Tabelle klasse erstellen
sql = """
CREATE TABLE klasse (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
"""
cursur.execute(sql)
connection.commit()
connection.close()
