# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import time
import os

def find_by_title(type, title, context):
    title = context.find(text=title)
    value = title.findNext(type).text
    return value

def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail

def blob_to_file(blob):
    ts = int(time.time()*10)
    route = './tmp/' + str(ts) + '.gif'
    file = open(route, 'wb')
    file.write(blob.decode('base64'))
    file.close()
    return route

def ensure_dir(file_path):
    if not os.path.exists(file_path):
        os.mkdir(file_path)


def extract_limits(raw_day):
    day = {}
    t = raw_day.split('/')
    if len(t) == 2:
        day['start'] = t[0]
        day['end'] = t[1]
        return day

    day['start'] = 0
    day['end'] = 0
    return day