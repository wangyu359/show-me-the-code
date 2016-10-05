# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:04:49 2016

@author: wys
"""

import re

def words_num(file_path):
  num = 0
  f = open(file_path,'r')
  for line in f:
    words_list = re.findall(r'[a-zA-Z0-9\']+',line)
    num += len(words_list)
  f.close()
  return num
  
if __name__ == '__main__':
  file_path = r'D:/show-me-the-code/0004.txt'
  print(words_num(file_path))
