import urllib

url = "http://tutorial-haartraining.googlecode.com/svn/trunk/data/negatives/"
html = urllib.urlopen(url).read()
tmp = html.find('href="')
html = html[tmp+6:]

num = 0
while(1):
    tmp = html.find('href="')
    tmpend = html.find('.jpg"')
    if tmpend == -1:
        break
    text = html[tmp+6:tmpend+4]
    html = html[tmpend+5:]

    print text

    f = open("negs_%d.jpg" % num,'wb')
    f.write(urllib.urlopen(url+text).read())
    f.close()

    num = num + 1

for i in range(0, num):
    print "negs_%d.jpg" % i
