# -*- coding: utf-8 -*-

import common as Common
import os
from bs4 import BeautifulSoup
import json

def get_user(context_page):
    data = {}
    
    data['id'] = Common.find_by_title('span', 'ID:', context_page)
    data['name'] = context_page.find('span', {'class': 'aligh-right color-white'}).text
    data['major'] = find_by_title('span', 'Programa', context_page)
    data['academic_condition'] = find_by_title('span', 'Condición Académica', context_page)
    data['starting_quarter'] = find_by_title('span', 'Trimestre Ingreso', context_page)
    data['last_quarter'] = find_by_title('span', 'Última Condición', context_page)
    data['quarter_index'] = find_by_title('span', 'Índice Trimestral', context_page)
    data['general_index'] = find_by_title('span', 'Índice General', context_page)
    data['validated_credits'] = find_by_title('span', 'Créditos Convalidados', context_page)
    data['aproved_credits'] = find_by_title('span', 'Créditos Aprobados', context_page)
    data['quarter_count'] = find_by_title('span', 'Trimestres Cursados', context_page)
    data['adviser'] = context_page.find('a', {'class': 'consejero-text'}).findChild().text

    Common.ensure_dir('./tmp')
    blob = context_page.find('div', {'class': 'circle-img'})['style']
    blob = Common.replace_last(blob.replace('background-image:url(data:image/gif;base64,', ''), ')', '')
    data['profile_picture'] = Common.blob_to_file(blob)
    
    return json.dumps(data)