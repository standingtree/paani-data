import os
import sys

import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Required to load the previously defined environment variables

# Create connection to postgres
connection = psycopg2.connect(host=os.environ.get('PG_HOST'),
                              port=os.environ.get('PG_PORT'),
                              user=os.environ.get('PG_USER'),
                              password=os.environ.get('PG_PASSWORD'),
                              dbname=os.environ.get('PG_DATABASE'))

connection.autocommit = True  # Ensure data is added to the database immediately after write commands
cursor = connection.cursor()
cursor.execute('SELECT %s as connected;', ('Connection to postgres  successful!',))
print(cursor.fetchone())

# create an empty table
createTableQuery = """
    CREATE TABLE IF NOT EXISTS my_table(
        id BIGSERIAL PRIMARY KEY NOT NULL,
        name varchar,
        date TIMESTAMP NOT NULL DEFAULT current_timestamp
        );
"""
# add it to the database
cursor.execute(createTableQuery)

# add data to the table
addDataQuery = 'INSERT INTO my_table(name) VALUES(%s);'
yourName = sys.argv[1] if len(sys.argv) > 1 else "viren"
cursor.execute(addDataQuery, (yourName,))

# read data from database
readDataQuery = 'SELECT * FROM my_table WHERE name = %s;'
cursor.execute(readDataQuery, (yourName,))
for record in cursor.fetchall():
    print(record)


# clean-up / delete data and table
deleteRecord = 'DELETE FROM my_table WHERE id=1;'
cursor.execute(deleteRecord)
readDataQuery = 'SELECT * FROM my_table WHERE name=%s;'
cursor.execute(readDataQuery, ('viren',))
for record in cursor.fetchall():
    print(record)

deleteTable = 'DROP TABLE IF EXISTS my_table;'
cursor.execute(deleteTable)

# close cursor and connection
cursor.close()
connection.close()
