import datetime
import shutil
import os
import pandas as pd
from sqlalchemy import create_engine, inspect
import psycopg2
import pyodbc
import re

# Variables
Server = ''  # Insert the server name or IP address
Database = ''  # Insert the database name
username = ""  # Insert the username
password = ''  # Insert the password
Driver = 'ODBC Driver 17 for SQL Server'
table_name = ''  # Insert the table name
pk_column_name = ''  # Insert the primary key column name
tmp_dir_path = ""  # Insert the temporary directory path
data_dir_path = ""  # Insert the data directory path

### Data cleaning 

# Grab files
data_files = [f for f in os.listdir(data_dir_path) if '.csv' in f.lower()]
new_file = data_files[-1]  # Get the newest file based on the modified time

# Clean dir and move file
shutil.rmtree(tmp_dir_path)  # Remove the temporary directory if it exists
os.mkdir(tmp_dir_path)  # Create the temporary directory
dest = tmp_dir_path + '/' + new_file
shutil.copy(data_dir_path + '/' + new_file, dest)  # Copy the newest file to the temporary directory
df = pd.read_csv(tmp_dir_path + '/' + new_file)  # Read the data into a DataFrame

# Data manipulation
df[pk_column_name] = pd.to_datetime(df[pk_column_name], dayfirst=True).apply(lambda s: s.isoformat())
df.to_csv(tmp_dir_path + '/' + new_file, index=False)  # Save the modified DataFrame back to the temporary file

### SQL logic

# Database connection
Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'
engine = create_engine(Database_con)
con = engine.connect()

# Read existing data from the database
df = pd.read_sql_query(f"SELECT * FROM [stirling_db].[dbo].[{table_name}]", con)

# Read new data from the CSV file
dp = pd.read_csv(tmp_dir_path + '/' + new_file)
dp.columns = [re.sub(r'[-\s/]+', '_', col.strip()).strip('_').replace('(', '').replace(')', '') for col in dp.columns]
dp.columns = [re.sub(r'[^a-zA-Z0-9_]', '', col) for col in dp.columns]

# Check if table exists
inspector = inspect(engine)
table_exists = inspector.has_table(table_name)

if table_exists:
    # Check for duplicates
    existing_times_query = f"SELECT {pk_column_name} FROM {table_name}"
    existing_times = pd.read_sql(existing_times_query, engine)

    # Convert the primary key column values to match the database format
    dp[pk_column_name] = pd.to_datetime(dp[pk_column_name]).dt.strftime('%Y-%m-%d %H:%M:%S')

    # Filter out duplicates
    dp_filtered = dp[~dp[pk_column_name].astype(str).isin(existing_times[pk_column_name].astype(str))]
else:
    dp_filtered = dp

# Ensure none of the column names end with an underscore
dp_filtered.columns = [col.rstrip('_') if col.endswith('_') else col for col in dp_filtered.columns]

# Write the DataFrame to the SQL table
dp_filtered.to_sql(table_name, engine, if_exists='append', index=False)
