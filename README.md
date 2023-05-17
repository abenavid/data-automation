# data-automation
1. web-scrape.py
 > * This is optional if you need to scrape the web to ingest .csv files into your local server
2. init-py-dataclean.py
 > *  Used to modify .csv files into appropriate format (i.e. removing unwanted rows/columns, changing date to SQL readable format, etc.)
 > *  Creates copy of .csv file in a temp folder where ETL pipeline will grab from and set data into SQL DB
3. SSIS project to move .csv file from tmp folder into SQL Server
4. Create Windows Taks Scheduler for init-pyh-dataclean.py
>  * you can use this to repeat however frequently you need
5. Create ETL Pipeline
>  * similar to step 4, but this triggers the SSIS script
6. Display your data from SQL Database via PowerBI
 
