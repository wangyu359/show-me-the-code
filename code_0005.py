# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:18:07 2016

@author: wys
"""

from PIL import Image
import os

def image_process(image_source):
  rate = max(image_source.size[0]/640.0 if image_source.size[0]>640 else 0,\
             image_source.size[1]/1136.0 if image_source.size[1]>1136 else 0)
  if rate:
    image_source.thumbnail((image_source.size[0]/rate, image_source.size[1]/rate))
  return image_source
  
def image_walk(read_path, write_path):
  os.chdir(read_path)
  for i in os.listdir(os.getcwd()):
    postfix = os.path.splitext(i)[1]
    if postfix == '.jpg' or postfix == '.png':
      image_source = Image.open(i)
      image_destination = image_process(image_source)
      image_destination.save(write_path + i)
      
if __name__ == '__main__':
  read_path = r'D:/show-me-the-code/0005_read/'
  write_path = r'D:/show-me-the-code/0005_write/'
  image_walk(read_path,write_path)
