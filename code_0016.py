# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 08:36:47 2016

@author: 
"""

import os
import json
import xlwt
from collections import OrderedDict

def txt2xls(file_path):
  os.chdir(file_path)
  
  # 'for line in file_handle:' is the fastest way to read the file, including big and small file
  # if there exists messy code, read it as bytes, then decode() it
  with open('0016.txt','rb') as f:
    content = f.read().decode()
    
  # convert to json(javascript object notation)
  #data_json = json.loads(content,object_pairs_hook=OrderedDict)
  data_json = json.loads(content)
  file = xlwt.Workbook()
  
  # add sheet
  table = file.add_sheet('number')
  for row,line in enumerate(data_json):
    # table.write(row,0,line)
    for col,vertical in enumerate(line):
      print(col,':',vertical)
      table.write(row,col,vertical)
  file.save('number.xls')
  
if __name__=='__main__':
  file_path = r'C:/Users/王宇树/Documents/wys/show-me-the-code/'
  txt2xls(file_path)
