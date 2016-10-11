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
  with open(file_path+'0014.txt','rb') as f:
    content = f.read().decode()
    
  # convert to json(javascript object notation)
  data_json = json.loads(content,object_pairs_hook=OrderedDict)
  file = xlwt.Workbook()
  
  # add sheet
  table = file.add_sheet('student')
  for row,line in enumerate(data_json):
    table.write(row,0,line)
    for col,vertical in enumerate(data_json[line]):
      table.write(row,col+1,vertical)
  file.save('student.xls')
  
if __name__=='__main__':
  file_path = r'C:/Users/王宇树/Documents/wys/show-me-the-code/'
  txt2xls(file_path)
