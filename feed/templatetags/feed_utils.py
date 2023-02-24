from urllib.parse import urlparse

from django import template

register = template.Library()


def getloc(value):
    domain = urlparse(value).netloc
    return domain


register.filter("getloc", getloc)
