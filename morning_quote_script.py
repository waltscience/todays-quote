# load quote database, select random quote, remove quote and update database
import pandas
import random
df = pandas.read_csv('~FILEPATH/Quote_db_good_genres_w_daily_removal.csv')
samp = random.randint(0, len(df))
quote = df.iloc[samp]["QUOTE"]
name = df.iloc[samp]["AUTHOR"]
df_update = df.drop([samp])
#df_update.to_csv('Quote_db_good_genres_w_daily_removal.csv')

# scrape image url from nature picture of the day website
import requests  
from bs4 import BeautifulSoup  
    
def getdata(url):  
    r = requests.get(url)  
    return r.text  
    
htmldata = getdata("https://www.naturepicoftheday.com/")  
soup = BeautifulSoup(htmldata, 'html.parser')  
#for item in soup.find_all('img'): 
#    print(item['src'])
s = soup.find_all('img')[0]
url = "https://www.naturepicoftheday.com/" + (s['src'])

# create markdown file that will be rendered as webpage in Jekyll
f = open("/Users/chriswalter/Documents/GitHub/waltscienceblog.github.io/quote.md","w+")
f.write('Quote of the day\r')
f.write("\r")
f.write('***\r')
f.write("\r")
f.write("## {}\r".format(quote))
f.write("\r")
f.write(" - ### {}\r".format(name))
f.write("\r")
f.write('***\r')
f.write('<img src=' + '"{}"'.format(url) + ' alt="Nature picture of the day">')

# use your twilio account script, id, and key from
# https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python
