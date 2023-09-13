import pandas as pd
from sqlalchemy import create_engine

# Create DB engine
engine = create_engine('sqlite:///sql/mydb.db')

# Read table from db to pandas
data_df = pd.read_sql_table('example_table', con=engine)
print(data_df)
