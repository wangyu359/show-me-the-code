# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:12:55 2016

@author: 
"""

def filterwords(input_words):
  sensitivity = 0
  words = []
  f = open(r'C:/Users/王宇树/Documents/wys/show-me-the-code/filtered_words.txt', 'rb')
  for l in f:
    words.append(l.decode('utf8'))
    
  for w in range(len(words)):
    if input_words.find(words[w].strip()) > -1: # if exists, then 0, if not, then -1
      sensitivity = 1
      break
  if sensitivity == 1:
    print('freedom')
  else:
    print('human rights')
      
if __name__ == '__main__':
  while(True):
    input_words = input('enter your words:') 
    if input_words == '':
      break
    filterwords(input_words)      
