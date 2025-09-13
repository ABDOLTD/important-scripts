# list_tables.py
import sqlite3, sys
db = "ndb.sqlite3"  # change to the full path if needed
conn = sqlite3.connect(db)
rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()
for (name,) in rows:
    print(name)
conn.close()
