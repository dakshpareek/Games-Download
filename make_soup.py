import requests
import ssl
from bs4 import BeautifulSoup
from PIL import Image
import urllib, cStringIO
import cgi
from pickle import dump
import json
import time
start_time = time.time()

def make__soup(url):
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
    except:
        return None
    return BeautifulSoup(html,"lxml")