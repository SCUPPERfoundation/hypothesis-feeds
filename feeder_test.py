from feeds import db
from feeds.models.alpha import ReviewDoc
import feedparser

gnews = 'https://news.google.com/rss/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen'

d = feedparser.parse(gnews)

for doc in d.entries:
    db.session.add(ReviewDoc(blob=doc))

db.session.commit()

