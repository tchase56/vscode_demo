import pandas as pd
from sqlalchemy import create_engine

# DB information
username = 'postgres'
password = 'mysecretpassword'
server = 'ip_address'
port = 'port'
database = 'demo_db'
uri_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(username, password, server, port, database)
engine = create_engine(uri_string)

# Create DataFrame
data_df = pd.DataFrame(
    {
        "numbers": [1,2,3,4,5,6,7,8,9],
        "letters": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    }
)

# Write dataframe to db
data_df.to_sql('example_table', con=engine, schema='public')
