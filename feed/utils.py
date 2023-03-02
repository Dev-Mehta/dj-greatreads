import os
import sys
from datetime import datetime
from pathlib import Path
from time import mktime
from urllib.parse import urlparse

import django
import feedparser

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings"

django.setup()

from feed.models import Post


def getloc(value):
    return urlparse(value).netloc


def parse_feeds():
    # top = feedparser.parse("https://hackernoon.com/tagged/hackernoon-top-story/feed")
    feed_django = feedparser.parse("https://hackernoon.com/tagged/django/feed")
    feed_python = feedparser.parse("https://hackernoon.com/tagged/python/feed")
    feed_simplified_web = feedparser.parse("https://simplifiedweb.netlify.app/rss.xml")
    feed_django = feed_django["entries"]
    feed_python = feed_python["entries"]
    feed_simplified_web = feed_simplified_web["entries"]
    feed_testdrivenio_django = feedparser.parse(
        "https://testdriven.io/blog/topics/django/feed.xml"
    )
    feed_testdrivenio_python = feedparser.parse(
        "https://testdriven.io/blog/topics/python/feed.xml"
    )
    feed_testdrivenio_docker = feedparser.parse(
        "https://testdriven.io/blog/topics/docker/feed.xml"
    )
    feed_testdrivenio_testing = feedparser.parse(
        "https://testdriven.io/blog/topics/testing/feed.xml"
    )

    feed_testdrivenio = (
        feed_testdrivenio_django["entries"]
        + feed_testdrivenio_docker["entries"]
        + feed_testdrivenio_python["entries"]
        + feed_testdrivenio_testing["entries"]
    )

    feed_hn_top_20 = feedparser.parse(
        "https://hackernoon.com/tagged/hackernoon-top-story/feed"
    )
    feed_hn_top_20 = feed_hn_top_20["entries"][:20]
    for f in feed_python:
        p_exists = Post.objects.filter(title=f.title).exists()
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
        else:
            break
    for f in feed_django:
        p_exists = Post.objects.filter(title=f.title).exists()
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
        else:
            break
    for f in feed_simplified_web:
        p_exists = Post.objects.filter(title=f.title).exists()
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
        else:
            break
    for f in feed_testdrivenio:
        p_exists = Post.objects.filter(title=f.title).exists()
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
        else:
            break
    for f in feed_hn_top_20:
        p_exists = Post.objects.filter(title=f.title).exists()
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
        else:
            break


parse_feeds()
