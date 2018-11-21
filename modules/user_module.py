# -*- coding: utf-8 -*-

import common as Common
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
    
    return json.dumps(data)