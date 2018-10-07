# -*- coding: utf-8 -*-
import psycopg2

class LogAnaysis():
    '''
    The main class contains methods encapsulating all required SQL statements
     for data access
    '''
    def __init__(self, dbname):
        self.connStr = 'dbname=' + dbname
    
    def getCursor(self):
        '''
        create connection 
        Args:
            None
        Returns:
            The cursor 
        '''
        self.conn = psycopg2.connect(self.connStr)
        cursor = self.conn.cursor()
        return cursor

    def getMostPopularArticles(self, top):
        '''
        Get Most popular articles
        Args:
            top: the number of records that needed
        Returns:
            list of records
        '''
        cursor = self.getCursor()
        sqlStr = 'select title, count(title) as views from ' + \
        'accessed_articles group by title order by views desc ' + \
        'limit %s;' % (top)
        cursor.execute(sqlStr)
        results = cursor.fetchall()
        self.conn.close()
        return results

    def getMostPopularAuthors(self):
        cursor = self.getCursor()
        sqlStr = 'select author_name, count(author_name) as views ' + \
        'from accessed_articles group by author_name order by views desc;'
        cursor.execute(sqlStr)
        results = cursor.fetchall()
        self.conn.close()
        return results
    
    def getMostErrorsDay(self):
        cursor = self.getCursor()
        sqlStr = "select access_date, round(((select sum(access) from " + \
        "statistic where status != '200 OK' and access_date = " + \
        "s.access_date)::numeric/(select sum(access) from statistic where " + \
        "access_date = s.access_date)::numeric)*100,2) as errorpercentage " + \
        "from statistic as s group by access_date having " + \
        "round(((select sum(access) from " + \
        "statistic where status != '200 OK' and access_date = " + \
        "s.access_date)::numeric/(select sum(access) from statistic where " + \
        "access_date = s.access_date)::numeric)*100,2) > 1 order by errorpercentage " + \
        "desc;"
        cursor.execute(sqlStr)
        results = cursor.fetchall()
        self.conn.close()
        return results


if __name__ == "__main__":
    logAnaysis = LogAnaysis('news')
    print('1. What are the most popular three articles of all time?')
    for r in logAnaysis.getMostPopularArticles(3):
        print('\"%s\" — %s views' % r)

    print('2. Who are the most popular article authors of all time?')
    for r in logAnaysis.getMostPopularAuthors():
        print('%s — %s views' % r)

    print('3. On which days did more than 1% of requests lead to errors?')
    for r in logAnaysis.getMostErrorsDay():
        print('%s — %s%% errors' % r)
