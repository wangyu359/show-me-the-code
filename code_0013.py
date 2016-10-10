# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 22:00:31 2016

@author: 
"""

import urllib
from bs4 import BeautifulSoup
import re

def crawler_girl(url, save_path):
  proto, rest = urllib.request.splittype(url) # protocal
  domain = urllib.request.splithost(rest)[0] #domain
  
  headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) \
             Gecko/20091201 Firefox/3.5.6',\
             'Referer': proto+'://'+domain} #'http://tieba.baidu.com'
  req = urllib.request.Request(url = url, headers = headers)
  html = urllib.request.urlopen(req).read()
  
  # non-greedy mode to find all the picture, BS would not work here because the html is not normal
  p = re.compile('<img.+?class="BDE_Image".+?>')
  list_of_pic = p.findall(html.decode()) # need decode
  
  counter = 1
  for l in list_of_pic:
    soup = BeautifulSoup(l,'lxml')
    url_img = soup.img['src']
    req_img = urllib.request.Request(url = url_img, headers = headers)
    pic = urllib.request.urlopen(req_img).read()
    postfix = url_img[url_img.rfind('.'):] # get the postfix of the picture file
                               # rfind return the final position '.' showing, else return -1
    # print postfix
#    file = open(save_path+str(counter)+postfix,'w')
#    try:
#      file.write(pic)
#    finally:
#      file.close()
      
    with open(save_path+str(counter)+postfix,'wb') as f:
      f.write(pic) # after read(), need decode()
    counter += 1
    
if __name__ == '__main__':
  url = 'http://tieba.baidu.com/p/2166231880'
  save_path = r'C:/Users/王宇树/Documents/wys/show-me-the-code/0013/'
  crawler_girl(url,save_path)
