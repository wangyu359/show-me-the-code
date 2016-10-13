# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:11:43 2016

@author: 
"""

import xlrd
import re

def phone_record(file_path):
  xls = xlrd.open_workbook(file_path)
  sheet = xls.sheet_by_index(0)
  
  initiative_call = 0
  passive_call = 0
  
  for line in range(13, sheet.nrows):
    data = sheet.row_values(line)
    struct_time = re.findall('\d+\.?\d*',data[2])
    struct_time = struct_time[::-1]
    if data[4] == '被叫':
      for i,v in enumerate(struct_time):
        passive_call += float(v)*60**i
    if data[4] == '主叫':
      for i,v in enumerate(struct_time):
        initiative_call += float(v)*60**i
  print('主叫时长：%d min'%(initiative_call/60))
  print('被叫时长：%d min'%(passive_call/60))
  
if __name__ == '__main__':
  file_path = r'C:/Users/王宇树/Documents/wys/show-me-the-code/0020.xls'  
  phone_record(file_path)
      
