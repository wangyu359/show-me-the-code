# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:12:55 2016

@author: 
"""

def filterwords(input_words):
  sensitive_words = []
  words = []
  f = open(r'C:/Users/王宇树/Documents/wys/show-me-the-code/filtered_words.txt', 'rb')
  for l in f:
    words.append(l.decode('utf8'))
    
  for w in words:
    if input_words.find(w.strip()) > -1: # if exists, then 0, if not, then -1
      sensitive_words.append(w.strip())      
  for w in sensitive_words:
    input_words = input_words.replace(w,'**')
  print(input_words)
    
      
if __name__ == '__main__':
  while(True):
    input_words = input('enter your words:') 
    if input_words == '':
      break
    filterwords(input_words)   
