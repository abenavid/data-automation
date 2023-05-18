Use Master 
GO
 
Create Database SSIS_FileData 
GO 

USE SSIS_FileData 
GO 

CREATE TABLE Customer_Data 
( 
  Name Nvarchar(400), 
  city nvarchar(200), 
  Address nvarchar(1000) 
) 
GO 