import sqlite3
connection = sqlite3.connect('schule.db')
cursor = connection.cursor()

# Die Namen aller Schüler:innen der Klasse I1A
sql = """
SELECT vorname, nachname
FROM schueler
JOIN klasse
ON klasse.id = schueler.klasse_id
WHERE klasse.name = "I1A"
"""
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row[0], row[1])
connection.close()
