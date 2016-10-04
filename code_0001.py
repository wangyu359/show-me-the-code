# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:21:42 2016

@author: wys

the problem is I cann't garantee that there are no repeated keys
"""

import random

def key(length):
  key_string = ''
  for l in range(length):
    # add '-' for every four character
    if l%4 == 0:
      if l != 0:
        key_string = key_string + '-'
      
    # three types: uppercase, lowercase, digit
    label1 = random.randint(1,3)
    if label1 == 1:
      label2 = random.randint(0,25)
      key_character = chr(ord('a')+label2)
      key_string = key_string + key_character
    if label1 == 2:
      label2 = random.randint(0,25)
      key_character = chr(ord('A')+label2)
      key_string = key_string + key_character
    if label1 == 3:
      label2 = random.randint(0,9)
      key_character = chr(ord('0')+label2)
      key_string = key_string + key_character
  return key_string
  
if __name__ == '__main__':
  key_num = 200
  key_len = 16
  key_list = []
  
  file_handle = open('D:/show-me-the-code/0001.txt','w')
  for i in range(key_num):
    key_list.append(key(key_len))
    file_handle.write(key(key_len)+'\n')
  file_handle.close()
      
