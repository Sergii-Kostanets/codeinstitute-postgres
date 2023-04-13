import psycopg2


# connect to 'chinook' database
connection = psycopg2.connect("chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the 'Artist' table
cursor.execute('SELECT * FROM "Artist"')

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# result = cursor.fetchone()

# close the connection
connection.close()

# print the results
for result in results:
    print(result)
