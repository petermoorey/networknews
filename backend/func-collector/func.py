from datetime import datetime, timedelta
from time import mktime
from os.path import dirname
import feedparser


with open(dirname(__file__) + '/data-sources.txt') as f:
    urls = f.read().splitlines()

for rss_url in urls:
    feed = feedparser.parse(rss_url)

    # if feed has been updated in last 7 days
    feed_updated_date = datetime.fromtimestamp(mktime(feed['feed']['updated_parsed']))
    if feed_updated_date + timedelta(days=7) > datetime.today():

        for item in feed['entries']:

            # if article was created in last 7 days
            publish_date = datetime.fromtimestamp(mktime(item.published_parsed))
            if publish_date + timedelta(days=7) > datetime.today():
                print(item)