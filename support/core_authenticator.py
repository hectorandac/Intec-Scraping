# This module gets the main page after logging with the user credentails

import mechanize
import urllib2 
from bs4 import BeautifulSoup
import cookielib

# Gets the context information page

def get_context(id, password):
    cj = cookielib.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.open("https://procesos.intec.edu.do/")

    br.select_form(nr=0)
    br.form['txtID'] = id
    br.form['txtUserPass'] = password
    br.submit()
    return br