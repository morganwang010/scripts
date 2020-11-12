import requests
from bs4 import BeautifulSoup
from pathlib import Path
import re
from urllib.parse import unquote
url="https://soft.ryana.cn/eBook/"
r = requests.get(url,verify=False)
r.encoding="utf-8"
#print(r.content.decode('gbk2312'))
#print(r.text)
soup = BeautifulSoup(r.text,"html.parser")
links = soup.findAll('a')
p = "^\\d"
i = 1 
def downloadpdf(links):
    for link in links:
        file_name = unquote(str(link.split('/')[-1]))
        name = "/root/" + file_name
        r3 = requests.get(link,stream = True)
        with open(name,"wb") as f:
            for chunk in r3.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)
    return

for link in links:
    if(re.match(p,link['href'])):
        #print(link['href'])
        newUrl = url + link['href']
        print(newUrl)
        r1 = requests.get(newUrl,verify=False)
        r1.encoding = "utf-8"
        s1 = BeautifulSoup(r1.text,"html.parser")
        
        links2 = s1.findAll("a")
        
        pdflinks = [newUrl + pl['href'] for pl in links2 if pl['href'].endswith('pdf')]
        downloadpdf(pdflinks) 
        #print(pdflinks)
 




