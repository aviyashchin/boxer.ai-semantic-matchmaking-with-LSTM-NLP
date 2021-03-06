import pandas as pd
import re
import mysql.connector as msc
# import os

# print os.getcwd()
#vcsites = pd.read_csv('private_funds.csv', sep='|')
#susites = pd.read_csv('startups.csv')
#domains = vcsites.Web.dropna()

config = {
   'user': 'root',
   'password': 'uLFZ2WoB',
   'host': '130.211.154.93',
   'database': 'test',
   'charset': 'utf8'
}

#Need to put this into an infinite loop
con = msc.connect(**config)
cur = con.cursor()
#con.autocommit(True)
#time.sleep(5)

#FIND A RANDOM 10 WEBSITES TO CRAWL FROM THE VC LIST
cur.execute("SELECT siteurl FROM vctest4 where ifnull(siteurl, '') <> '' and ifnull(text, '') = '' ORDER BY RAND() LIMIT 10;")

test = cur.fetchall()
test = [list(row)[0] for row in map(list, test)]
test2 = pd.Series(test)

domains = test2.apply(lambda x: re.sub(r'((http(s)?://)?(www.)?)', '', x.lower())).tolist()
urls = map(lambda domain: 'http://www.' + domain, domains)

#FIND A RANDOM 10 WEBSITES TO CRAWL FROM THE STARTUP LIST
cur.execute("SELECT siteurl FROM crunchbase_startups where ifnull(siteurl, '') <> '' and ifnull(text, '')  = '' ORDER BY RAND() LIMIT 10;")
sulist = cur.fetchall()
sulist = [list(row)[0] for row in map(list, sulist)]
sulist2 = pd.Series(sulist)

#domains_su = sulist2.domains.dropna()
domains_su = sulist2.apply(lambda x: re.sub(r'((http(s)?://)?(www.)?)', '', x.lower())).tolist()
urls_su = map(lambda domain: 'http://www.' + domain, domains_su)

con.close()
