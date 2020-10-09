import sqlite3
connection = sqlite3.connect('schule.db')
cursor = connection.cursor()

# Tabelle klasse erstellen
sql = """
CREATE TABLE IF NOT EXISTS klasse (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
"""
cursor.execute(sql)

# Tabelle schueler erstellen
sql = """
CREATE TABLE  IF NOT EXISTS schueler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vorname TEXT,
    nachname TEXT,
    klasse_id INTEGER,
    FOREIGN KEY (klasse_id) REFERENCES klasse(id)
)
"""
cursor.execute(sql)

connection.commit()
connection.close()
