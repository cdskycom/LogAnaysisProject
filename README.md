# Logs Anaysis Project

This is a reporting tool of a fake newspaper site, This tool can print the site's statistics data, includes:
1. What are the most popular three articles of all time?
   
2. Who are the most popular article authors of all time?
    
3. On which days did more than 1% of requests lead to errors?

There is just one file in the Project-log_anaysis.py

## Installation
- git clone https://github.com/cdskycom/LogAnaysisProject.git

## Python version
This project tested under python 3.6. It's recommendation to use 3.6 or above.
-Python Setup and Usage-follow this instruction to get python
 https://docs.python.org/3.6/using/index.html

## Database requirements
As noted previously, this tool depends on the specific running environment includes Python3 environment and specific database(PostgreSql). To test this tools, you'll need database software (We've already provided by a Linux virtual machine) and data to analyze. Please follow instructions below to get database and data.

- Installing the Virtual Machine
  https://classroom.udacity.com/nanodegrees/nd004-cn/parts/d3335c49-3556-488a-9f63-c0d28b16ff12/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0

- Download the data
  Next, download the data here(https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
  To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: (FSND version)
  To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
  Here's what this command does:
  
  psql — the PostgreSQL command line program
  -d news — connect to the database named news which has been set up for you
  -f newsdata.sql — run the SQL statements in the file newsdata.sql
  Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## Data views
This tool performs massive database queries and Dependents on specific views. In order to run this tool, you need create follow two views:

	create view accessed_articles as
    	select log.path, log.status, log.time, articles.title, articles.slug, authors.name as author_name
    	from log join articles on log.path = concat('/article/', articles.slug)
    	join authors on articles.author = authors.id;

	create view statistic as
    	select to_char(time, 'FMMonth DD,YYYY') as access_date,status,count(1) as access from log group by access_date,status;

## Usage:
Command Line

   - python log_anaysis.py 