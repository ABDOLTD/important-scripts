import sqlite3
import pandas as pd

# path to your sqlite database
conn = sqlite3.connect("ndb.sqlite3")

# table name (probably recording_modelname, check with sqlitebrowser or introspection)
df = pd.read_sql_query("SELECT * FROM app_recording;", conn)

df.to_csv("recording_export.csv", index=False)

conn.close()
print("Exported recording_export.csv")
