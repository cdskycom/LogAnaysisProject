# Logs Anaysis Project

This is a reporting tool of a fake newspaper site, This tool can print the site's statistics data, includes:
1. What are the most popular three articles of all time?
   
2. Who are the most popular article authors of all time?
    
3. On which days did more than 1% of requests lead to errors?

There is just one file in the Project-log_anaysis.py

## Installation
- git clone https://github.com/cdskycom/Movie-Trailer-Website.git

## Python version
This project tested under python 3.6. It's recommendation to use 3.6 or above.

## Database requirements
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