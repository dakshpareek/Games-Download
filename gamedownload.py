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
from pickle import load
import json
import time,os
import re
from make_soup import make__soup


start_time = time.time()

def make_soup(url,params):
    try:
        html = requests.post(url,params).content
    except:
        return None
    return BeautifulSoup(html,"lxml")

f=open("mygames.txt","r")
data=load(f)
f.close()

#finding id of movie
sid=os.environ['PATH_TRANSLATED']
id=sid.split('\\')
id=int(id[-1])
#print data[id][1]

link=data[id]

soup=make__soup(link)
form=soup.find("form")
x=form.find_all("input")
params={}
params['filename']=x[0].attrs['value']
params['filesize']=x[1].attrs['value']
params['id']=x[2].attrs['value']

#print params
url="http://solvettube.com/we-are-testing-this-game-and-video-guide-is-in-progress/"

soup=make_soup(url,params)
scripts=soup.findAll("script",type="text/JavaScript")
soup=scripts[0]
soup=str(soup)
s=soup[409:550]
print s
loc=s.find("';")
s=s[:loc]

#print "<a href='{}' download>Dowload</a>".format(s)
print s

print '''
</body>
</html>
'''