# todays-quote
Python script and data to generate daily motivational quotes and images.

## How to automate daily motivation with a little Python
### Author: Chris Walter - [Daily Motivational Quote Article](https://waltscienceblog.github.io/morningquote/)

Data sources: Quote database, curated by Akhil Tak, retrieved on Feb 6, 2021 from https://github.com/akhiltak/inspirational-quotes/blob/master/Quotes.csv

Image source: Nature picture of the day, scraped daily from http://www.naturepicoftheday.com/

Quote_db_original.csv - original quote database
Quote_db_good_genres.csv - quote database with motivational quote categories selected
Quote_db_good_genres_daily_removal.csv - quote database with daily quote removed once selected, to avoid repeating
Morning_quote_script.py - python script to select quote, scrape image, create daily markdown file for webpage, and text quote through SMS.
