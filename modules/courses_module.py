# -*- coding: utf-8 -*-
import common as Common
from bs4 import BeautifulSoup
import json

def get_courses_timetable_by_name(browser, name):
    #TODO: Enhance string pattern algorithm.

    name = name.upper()
    browser.find_link(url='/OfertaAcademica/Index')
    req = browser.click_link(url='/OfertaAcademica/Index')
    browser.open(req)

    oferta_academica = browser.response().read()
    soup = BeautifulSoup(oferta_academica, 'html.parser')
    signatures = []
    signatures_arr = []
    outter = soup.find('tbody', attrs={'class': 'title'})
    
    while outter != None:
        if name in outter.findAll('td')[1].text:
            signatures.append(outter)
        outter = outter.findNext('tbody', attrs={'class': 'title'})
    
    # Iterates each signature in the result
    for signature in signatures:
        signature_obj = {}
        heading = signature.findAll('td')
        general_title = heading[1].text.split('-')
        
        signature_obj['code'] = general_title[0]
        signature_obj['title'] = general_title[2]
        signature_obj['credits'] = heading[2].text

        # Gets the sections
        sections = []
        sections_raw = signature.findNext('tbody').find('tbody').findAll('tr')
        for section_raw in sections_raw:
            section_raw = section_raw.findAll('td')
            section = {}
            section['type'] = section_raw[0].text
            section['section'] = section_raw[1].text
            section['room'] = section_raw[2].text.split(',')
            section['teacher'] = section_raw[3].text
            section['monday'] = Common.extract_limits(section_raw[4].text)
            section['tuesday'] = Common.extract_limits(section_raw[5].text)
            section['wednesday'] = Common.extract_limits(section_raw[6].text)
            section['thursday'] = Common.extract_limits(section_raw[7].text)
            section['friday'] = Common.extract_limits(section_raw[8].text)
            section['saturday'] = Common.extract_limits(section_raw[9].text)            
            
            sections.append(section)

        signature_obj['sections'] = sections
        signatures_arr.append(signature_obj)

    return json.dumps(signatures_arr)


def get_course_timetable_by_id(browser, id):
    browser.find_link(url='/OfertaAcademica/Index')
    req = browser.click_link(url='/OfertaAcademica/Index')
    browser.open(req)

    oferta_academica = browser.response().read()
    soup = BeautifulSoup(oferta_academica, 'html.parser')
    signature = soup.find('tbody', attrs={'id': 'Asignatura-' + id})
    if(signature):
        signature_obj = {}

        heading = signature.findAll('td')
        general_title = heading[1].text.split('-')
        
        signature_obj['code'] = general_title[0]
        signature_obj['title'] = general_title[2]
        signature_obj['credits'] = heading[2].text

        # Gets the sections
        sections = []
        sections_raw = signature.findNext('tbody').find('tbody').findAll('tr')
        for section_raw in sections_raw:
            section_raw = section_raw.findAll('td')
            section = {}
            section['type'] = section_raw[0].text
            section['section'] = section_raw[1].text
            section['room'] = section_raw[2].text.split(',')
            section['teacher'] = section_raw[3].text
            section['monday'] = Common.extract_limits(section_raw[4].text)
            section['tuesday'] = Common.extract_limits(section_raw[5].text)
            section['wednesday'] = Common.extract_limits(section_raw[6].text)
            section['thursday'] = Common.extract_limits(section_raw[7].text)
            section['friday'] = Common.extract_limits(section_raw[8].text)
            section['saturday'] = Common.extract_limits(section_raw[9].text)            
            
            sections.append(section)

        signature_obj['sections'] = sections
        return signature_obj
    else:
        nothing = {}
        nothing['result'] = 'There is no course with the given id: ' + id
        return json.dumps(nothing)

def get_available_courses(browser):

    # Clicks the button for 'Oferta académica'
    browser.find_link(url='/OfertaAcademica/Index')
    req = browser.click_link(url='/OfertaAcademica/Index')
    browser.open(req)

    oferta_academica = browser.response().read()
    
    signatures_arr = []
    soup = BeautifulSoup(oferta_academica, 'html.parser')
    signatures = soup.findAll('tbody', attrs={'class': 'title'})

    # Iterates each signature in the result
    for signature in signatures:
        signature_obj = {}
        heading = signature.findAll('td')
        general_title = heading[1].text.split('-')
        
        signature_obj['code'] = general_title[0]
        signature_obj['title'] = general_title[2]
        signature_obj['credits'] = heading[2].text

        # Gets the sections
        sections = []
        sections_raw = signature.findNext('tbody').find('tbody').findAll('tr')
        for section_raw in sections_raw:
            section_raw = section_raw.findAll('td')
            section = {}
            section['type'] = section_raw[0].text
            section['section'] = section_raw[1].text
            section['room'] = section_raw[2].text.split(',')
            section['teacher'] = section_raw[3].text
            section['monday'] = Common.extract_limits(section_raw[4].text)
            section['tuesday'] = Common.extract_limits(section_raw[5].text)
            section['wednesday'] = Common.extract_limits(section_raw[6].text)
            section['thursday'] = Common.extract_limits(section_raw[7].text)
            section['friday'] = Common.extract_limits(section_raw[8].text)
            section['saturday'] = Common.extract_limits(section_raw[9].text)            
            
            sections.append(section)

        signature_obj['sections'] = sections
        signatures_arr.append(signature_obj)

    return json.dumps(signatures_arr)