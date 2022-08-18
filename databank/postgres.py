import os
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
