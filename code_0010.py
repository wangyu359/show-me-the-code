# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 22:01:48 2016

@author: 
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pylab import *
import random, numpy, string

def generate_identifying_code(path):
  text = random.sample(string.ascii_letters,4)
  
  # generate 3-D random array
  raw_array = numpy.zeros((100,300,3), dtype = numpy.uint8)
  array_shape = raw_array.shape
  for i in range(array_shape[0]):
    for j in range(array_shape[1]):
      for k in range(array_shape[2]):
        raw_array[i][j][k] = random.randint(0,255)
        
  # generate the background picture from 3-D array
  im = Image.fromarray(raw_array)
  draw = ImageDraw.Draw(im)
  
  # add check code onto the background
  for i in range(len(text)):
    draw.text((75*i+random.randint(0,40),random.randint(0,40)), text[i],\
              font = ImageFont.truetype('arial.ttf',60), \
              fill = (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
  im.save(path+'/checkcode.jpg')
  
if __name__ == '__main__':
  path = r'C:/Users/王宇树/Documents/wys/show-me-the-code'
  generate_identifying_code(path)
