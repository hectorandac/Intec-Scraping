# -*- coding: utf-8 -*-

import common as Common
import os
from bs4 import BeautifulSoup
import json

def get_user(context_page):
    data = {}
    
    data['id'] = Common.find_by_title('span', 'ID:', context_page)
    data['name'] = context_page.find('span', {'class': 'aligh-right color-white'}).text
    data['major'] = Common.find_by_title('span', 'Programa', context_page)
    data['academic_condition'] = Common.find_by_title('span', 'Condición Académica', context_page)
    data['starting_quarter'] = Common.find_by_title('span', 'Trimestre Ingreso', context_page)
    data['last_quarter'] = Common.find_by_title('span', 'Última Condición', context_page)
    data['quarter_index'] = Common.find_by_title('span', 'Índice Trimestral', context_page)
    data['general_index'] = Common.find_by_title('span', 'Índice General', context_page)
    data['validated_credits'] = Common.find_by_title('span', 'Créditos Convalidados', context_page)
    data['aproved_credits'] = Common.find_by_title('span', 'Créditos Aprobados', context_page)
    data['quarter_count'] = Common.find_by_title('span', 'Trimestres Cursados', context_page)
    data['adviser'] = context_page.find('a', {'class': 'consejero-text'}).findChild().text

    Common.ensure_dir('./tmp')
    blob = context_page.find('div', {'class': 'circle-img'})['style']
    blob = Common.replace_last(blob.replace('background-image:url(data:image/gif;base64,', ''), ')', '')
    data['profile_picture'] = Common.blob_to_file(blob)
    
    return json.dumps(data)

def get_timetable(context_page):
    table = context_page.find('table', {'id': 'tblActuales'})
    signatures = table.findAll('tr', {'class': 'header-tr'})
    signatures_arr = []
    for signature in signatures:
        raw_html = signature.findAll('td')
        signature_obj = {}

        signature_obj['code'] = raw_html[0].text
        signature_obj['name'] = raw_html[1].text
        signature_obj['section'] = raw_html[2].text
        signature_obj['location'] = raw_html[3].text.split(', ')
        signature_obj['monday'] = Common.extract_limits(raw_html[4].text)
        signature_obj['tuesday'] = Common.extract_limits(raw_html[5].text)
        signature_obj['wednesday'] = Common.extract_limits(raw_html[6].text)
        signature_obj['thursday'] = Common.extract_limits(raw_html[7].text)
        signature_obj['friday'] = Common.extract_limits(raw_html[8].text)
        signature_obj['saturday'] = Common.extract_limits(raw_html[9].text)

        signatures_arr.append(signature_obj)

    return json.dumps(signatures_arr)