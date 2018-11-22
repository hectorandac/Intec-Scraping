# -*- coding: utf-8 -*-
import common as Common
from bs4 import BeautifulSoup
import json

data = {}

def get_selected_subjects(context_page):
    actual_table = context_page.find('table', {'id': 'tblActuales'})
    rows = actual_table.find_all('tr') # all rows

    row_number = -1
    for r in rows:
        c = 1
        subject = {}
        schedule = {}
        for td in r.find_all('td'): # all columns (td) by row (r)
            value = td.text
            if value:
                if c == 1:
                    subject['code'] = value
                elif c == 2:
                    subject['name'] = value
                elif c == 3:
                    subject['section'] = value
                elif c == 4:
                    subject['room'] = value
                elif c == 5:
                    schedule['lun'] = value
                elif c == 6:
                    schedule['mar'] = value
                elif c == 7:
                    schedule['mie'] = value
                elif c == 8:
                    schedule['jue'] = value
                elif c == 9:
                    schedule['vie'] = value
                elif c == 10:
                    schedule['sab'] = value
                elif c == 11:
                    schedule['dom'] = value
                elif c == 12:
                    subject['teacher'] = value
                elif c == 13:
                    subject['evaluated'] = value
            c = c + 1
        if row_number > -1: # Avoiding header row to save into data dictionary
            subject['schedule'] = schedule
            data[row_number] = subject
        row_number = row_number + 1
    
    return json.dumps(data)