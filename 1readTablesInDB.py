import sqlite3

db_file = "sampleDB.db"

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [row[0] for row in cursor.fetchall()]

if tables:
    print("Tables in the database:")
    for table_name in tables:
        print(table_name)
else:
    print("No tables found in the database.")

conn.close()