# data-automation
1. web-scrape.py
 > * This is optional if you need to scrape the web to ingest .csv files into your local server
2. data-mover.py
 > *  Used to modify .csv files into appropriate format (i.e. removing unwanted rows/columns, changing date to SQL readable format, etc.)
 > *  Creates copy of .csv file in a temp folder where ETL pipeline will grab from and set data into SQL DB
 > *  Inserts data into SQL DB
3. Create Windows Taks Scheduler for data-mover.py
>  * you can use this to repeat however frequently you need
4. Display your data from SQL Database via PowerBI