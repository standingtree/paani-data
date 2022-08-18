import psycopg2 as ps

# postgres credentials
credentials = {
    'host': '', # endpoint
    'port': '', # port
    'username': 'VelesIndiaAdmin',
    'password': 'VelesIndia0815!',
    'database_name': 'veles-india-db1'
}

# create connection and cursor
conn = ps.connect(host=credentials['host'],
                  database=credentials['database_name'],
                  user=credentials['username'],
                  password=credentials['password'],
                  port=credentials['port']
                  )


cur = conn.cursor()
