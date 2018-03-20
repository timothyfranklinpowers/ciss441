#Powers, Timothy
import urllib2

mywedding = list()
mywedding.append(['PP','http://www.pronouncedpowers.com'])
mywedding.append(['ZL','http://www.zola.com'])
for myweddata in mywedding:

    mytype, mypageurl = myweddata
    response = urllib2.urlopen('http://python.org')
    html = response.read()
    print(mytype, mypageurl, html[0:300])
