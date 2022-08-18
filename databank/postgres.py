import psycopg2 as ps

# define credentials
credentials = {
    'POSTGRES_ADDRESS': '', # endpoint
    'POSTGRES_PORT': '', # port
    'POSTGRES_USERNAME': 'VelesIndiaAdmin',
    'POSTGRES_PASSWORD': 'VelesIndia0815!',
    'POSTGRES_DBNAME': 'veles-india-db1'
}

# create connection and cursor
conn = ps.connect(host=credentials['POSTGRES_ADDRESS'],
                  database=credentials['POSTGRES_DBNAME'],
                  user=credentials['POSTGRES_USERNAME'],
                  password=credentials['POSTGRES_PASSWORD'],
                  port=credentials['POSTGRES_PORT']
                  )


cur = conn.cursor()