# README
1. web-scrape.py
    - *Optional*: Use this script to scrape the web and ingest .csv files into your local server.
2. data-mover.py
    - Modify .csv files for appropriate formatting (e.g., remove unwanted rows/columns, change date to SQL readable format, etc.).
    - Create a copy of the .csv file in a temporary folder for the ETL pipeline to access and set data into the SQL DB.
    - Insert the data into the SQL DB.
3. Create Windows Task Scheduler for data-mover.py
    - Set up a scheduled task using Windows Task Scheduler to execute the data-mover.py script at the desired frequency.
4. Display your data from SQL Database via PowerBI

# Data Cleaning:
- Grab the list of files in the data directory with a .csv extension.
- Get the newest file based on the modified time.
- Clean the temporary directory by removing it if it exists and then creating a new one.
- Copy the newest file to the temporary directory.
- Read the data from the file into a DataFrame.
- Manipulate the data by converting the primary key column values to ISO format and save the DataFrame back to the file.

# SQL Logic:
- Establish a connection to the database using the provided server, database, and driver information.
- Read the existing data from the specified table into a DataFrame.
- Read the new data from the temporary file into a DataFrame.
- Clean the column names by replacing special characters and spaces with underscores.
- Check if the table exists in the database.
- If the table exists, retrieve the existing primary key values from the table.
- Convert the primary key column values in the new data to match the database format.
- Filter out duplicate rows based on the primary key column.
- If the table doesn't exist, use the entire new data.
- Ensure none of the column names end with an underscore.
- Write the filtered DataFrame to the specified table in the database.
