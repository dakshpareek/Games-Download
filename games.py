#!C:\Python27\python.exe 
print "Content-type:text/html\r\n\r\n"
print '''<html>
<head></head>
<body>
'''


import requests
import ssl
from bs4 import BeautifulSoup
from PIL import Image
import urllib, cStringIO
import cgi
from pickle import dump
import json
import time
import re
start_time = time.time()

def make__soup(url):
	try:
		html = requests.get(url).content
	except:
		return None
	return BeautifulSoup(html,"lxml")

url="http://oceanofgames.com"
soup=make__soup(url)
all_games=soup.find_all("a",{"class":"post-thumb"})
all_data=[]

for i,j in enumerate(all_games):
	print "<h3><a href='gamedownload.py/{}' >{}</a>".format(i,j.attrs['title'])
	all_data.append(j.attrs['href'])

f1=open('mygames.txt','w')
dump(all_data,f1)
f1.close()

print '''
</body>
</html>
'''