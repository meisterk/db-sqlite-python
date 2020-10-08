import sqlite3
connection = sqlite3.connect('schule.db')
cursur = connection.cursor()

# Daten in klasse erstellen
sql = """INSERT INTO klasse (name) VALUES ("I1A"), ("I3A"), ("T1A"), ("T3A")"""
cursur.execute(sql)
connection.commit()

# Daten in schueler erstellen
sql = """
INSERT INTO schueler (vorname, nachname, klasse_id)
VALUES
("Anna", "Arm", 1),
("Berta", "Bein", 1),
("Carla", "Copf", 2),
("Dieter", "Darm", 4)
"""
cursur.execute(sql)
connection.commit()

connection.close()
