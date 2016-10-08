# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:42:48 2016

@author: 
"""

from bs4 import BeautifulSoup
import urllib
#import urllib2 # no this module

url = 'http://www.baidu.com'
url = 'http://blog.csdn.net/huangxiongbiao/article/details/45584407'

def find_links(url):
  proto, rest = urllib.request.splittype(url) # protocal
  domain = urllib.request.splithost(rest)[0] #domain
  
  # to simulate the human visit
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
  req = urllib.request.Request(url=url, headers = headers)
  html = urllib.request.urlopen(req).read()

#  # machine visit
#  html = urllib.request.urlopen(url).read()
  
  a = BeautifulSoup(html,'lxml').findAll('a')
#  a = BeautifulSoup(html).find_all('a')
  
#  alist = [i.attrs['href'] for i in a if i.attrs['href'][0] != 'j'] # there may not have attribute href
  alist = [i.attrs['href'] for i in a if (i.has_attr('href') and i.attrs['href'][0] != 'j')]
  alist = map(lambda i:proto + '://' + domain + i if i[0]=='/' else\
              url + i if i[0]=='#' else i, alist)
  return alist
  
if __name__ == '__main__':
  for i in find_links(url):
    print(i)
