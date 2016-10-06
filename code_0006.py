# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:59:16 2016

@author: wys
"""

from collections import Counter
import re
import string
import os

def get_word(txt_file):
  stop_word = ['the','in','of', 'and', 'to', 'has', 'that', 'this','s', 'is', 'are', 'a', 'with', 'as', 'an']
  
  f = open(txt_file,'r')
  patten = '[a-z0-9\']+'
  
  # for small file
#  content = f.read().lower()  
#  words = re.findall(patten, content)
#  wordlist = Counter(words)  
  
  # for large file
  wordlist = Counter({})
  for i in f:
    content = i.lower()
    words = re.findall(patten,content)
    wordlist = wordlist + Counter(words)
  
  for i in stop_word:
    wordlist[i] = 0

  f.close()
  return wordlist.most_common()[0]

def file_walk(read_path):
  for txt_name in os.listdir(read_path):
    txt_file = os.path.join(read_path, txt_name)
    
    word_important = get_word(txt_file)
    print(word_important[0]+' is the most important word, and the using time is ' + str(word_important[1]))
    
if __name__ == '__main__':
  read_path = r'D:/show-me-the-code/0006/'
  file_walk(read_path)
