import sqlite3

db_file = "sampleDB.db"
table_name = "sampleTable"

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute(f"SELECT * FROM {table_name};")  # Use f-string for table name

rows = cursor.fetchall()

if rows:
    print(f"Data in {table_name}:")
    for row in rows:
        print(row)
else:
    print(f"No data found in {table_name}.")

conn.close()