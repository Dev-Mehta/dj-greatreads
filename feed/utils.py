import os
import sys
from datetime import datetime
from time import mktime
from urllib.parse import urlparse

import django
import feedparser

from feed.models import Post


sys.path.append("E:\\Devfiles\\DjNews")
os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings"

django.setup()


def getloc(value):
    return urlparse(value).netloc


def parse_feeds():
    # top = feedparser.parse("https://hackernoon.com/tagged/hackernoon-top-story/feed")
    ctx = feedparser.parse("https://hackernoon.com/tagged/django/feed")
    simplified_web = feedparser.parse("https://simplifiedweb.netlify.app/rss.xml")
    raddevus = feedparser.parse("https://hackernoon.com/feed/u/raddevus")
    olek = feedparser.parse("https://hackernoon.com/feed/u/oleksandrkaleniuk")
    feed = (
        ctx["entries"]
        + simplified_web["entries"]
        + raddevus["entries"]
        + olek["entries"]
    )
    # feed = top['entries'][:50]
    for f in feed:
        p_exists = Post.objects.filter(title=f.title).exists()
        print(p_exists)
        if not p_exists:
            dt = datetime.fromtimestamp(mktime(f["published_parsed"]))
            p = Post(
                title=f.title,
                summary=f.summary,
                link=f.link,
                author="",
                pub_at=dt.date(),
            )
            try:
                p.author = f.author
            except AttributeError:
                p.author = getloc(f.link)
            p.save()
            print(str(p) + "...created")


parse_feeds()
