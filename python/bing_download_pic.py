from bs4 import BeautifulSoup
import urllib.request
import requests
import time
import json
import sys
import re
import os

#爬取目标网站url
CRAWL_TARGET_URL = 'https://cn.bing.com/images/async?q=%s&first=%d&count=%d&relp=%d&lostate=r&mmasync=1'
CRAWL_TARGET_URL = 'https://cn.bing.com/images/search?q=%s&qs=n&form=QBIR&sp=-1&pq=%E5%90%8A%E8%A3%85&sc=0-2&cvid=2438AAE9118643BE8313561F80F507B4&first=1&scenario=ImageHoverTitle'
#每次抓取图片数量(35是此网页每次翻页请求数量)
NUMS_PER_CRAWL = 35
#抓取图片最小大小(单位字节)，小于此值抛弃
MIN_IMAGE_SIZE = 10


def get_image(url, path, count):
    try:
        u = urllib.request.urlopen(url, timeout=5)
        t = u.read()
        if sys.getsizeof(t) < MIN_IMAGE_SIZE:
            return -1
    except Exception as e:
        print(url, e)
        return -2
    #提取图片格式
    frmt = url[url.rfind('.'):]
    p = re.compile("^\\.[a-zA-Z]+")
    m = p.match(frmt)
    frmt = m.group(0)
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        f = open(os.path.join(path, str(count)+frmt), 'wb')
        f.write(t)
        f.close()
    except Exception as e:
        print(os.path.join(path, str(count)+frmt), e)
        return -3
    return 0


def crawl_data(info, num):
    first = 0
    count = 0
    #创建一个会话
    s = requests.Session()
    #创建文件路径
    path="./"+info
    if not os.path.exists(path):
        os.mkdir(path)
    index=len(os.listdir(path))#文件中原有图片数
    while(count < num):
        u = CRAWL_TARGET_URL%(info, first, NUMS_PER_CRAWL, NUMS_PER_CRAWL)
        #3.05s为发送超时时间，10s为接收到数据超时时间
        req = s.get(url =u, timeout=(3.05, 10))
        bf = BeautifulSoup(req.text, "html.parser")
        imgtags = bf.find_all("a", class_ = "iusc")
        for e in imgtags:
            if count == num:
                return False
            urldict = json.loads(e.get('m'))
            if get_image(urldict["murl"], path, index) < 0:
                continue
            print("Downloaded %d picture"%(count+1))
            sys.stdout.flush()
            count =count+1
            index=index+1
            time.sleep(0.01)
        first = first + NUMS_PER_CRAWL
        time.sleep(0.1)

    return True

if __name__ == '__main__':
    
    # 关键词，可设置为多个
    key_words=['吊装',]
    # 下载的图片数量
    picture_num = 300

    for i in range(len(key_words)):
        word=key_words[i]
        print(word)
        if crawl_data(word, picture_num):
            i=i+1