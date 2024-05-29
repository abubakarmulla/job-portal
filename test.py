import sqlite3
con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
data = [
    (4,"Administration and management"),
    (5,"Computing and ICT"),
    (6,"Construction and building"),
    (7,"Design and arts"),
    (8,"Education and training"),
    (9,"Engineering"),
    (10,"Facilities and property services"),
    (11,"Financial services"),
    (12,"Legal and court services"),
    (13,"Retail and customer services"),
    (14,"Security and protective services"),
    (15,"Transport, distribution and logistics")
]
# cur.executemany("INSERT INTO jobapp_category VALUES(?, ?)", data)
cur.execute("UPDATE jobapp_job set is_published = 1 where id = 1 ;")
con.commit()
con.close()