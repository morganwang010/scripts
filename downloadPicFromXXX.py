import uuid
import json
import urllib.request
import string
import sys,time  
import os
import socket  
import random
import threading
import os,re,sys
targetDir = r"C:\pic500"  
def destFile(path):  
    if not os.path.isdir(targetDir):  
        os.mkdir(targetDir)  
    pos = path.rindex('/')
    a = random.randint(1,10000)
    ss = uuid.uuid1()
    b = '%d' %a  
    ss = uuid.uuid1()
    ss = str(ss)[:8]
    t = os.path.join(targetDir,  b+ss+path[pos+1:]) 
    return t  

def getPic(link):
    try:
        urllib.request.urlretrieve(link, destFile(link))
    except:
        pass     
		
def urlOpen(url):
	try:
        u = urllib.request.urlopen(url)
    except:
        pass
	d = json.loads(u.read().decode())
    t = re.findall(r'([^\s]*(\/))',d['thumbnail_url'])
	link = t[0][0] + '2048.jpg'
	try:
        urllib.request.urlretrieve(link, destFile(link))
    except:
        pass 
		
if __name__ == "__main__":  
    m = 0
    threads = []
    threadsOpen = []
    for i in range(71947476,71999999):
        url='http://500px.com/photo/%d/oembed.json' %i
        socket.setdefaulttimeout(5)
        if(m<10):
            th = threading.Thread(target = urlOpen,args=(url,))
            threads.append(th)
            m=m+1
            continue
        else:
            for s in range(m):
                threads[s].start()
            m = 0
            threads = []
        #time.sleep(4)
         
        
   