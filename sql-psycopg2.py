import os
import psycopg2
if os.path.exists("env.py"):
    import env


password = os.environ.get("PASSWORD")


# Define the connection parameters
connection_params = {
    "dbname": "chinook",
    "host": "localhost",  # for local development only
    "port": 5432,  # for local development only
    "user": "postgres",  # for local development only
    "password": password  # for local development only
}

# connect to 'chinook' database
connection = psycopg2.connect(**connection_params)

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 from the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print the results
for result in results:
    print(result)
