# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

def find_by_title(type, title, context):
    title = context.find(text=title)
    value = title.findNext(type).text
    return value