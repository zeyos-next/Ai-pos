import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('your_database.db')

# Create a cursor object
cursor = conn.cursor()

# Query to list all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all table names
tables = cursor.fetchall()

# Print out the table names
print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the connection
conn.close()
