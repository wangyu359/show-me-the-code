# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:59:50 2016

@author: 
"""

import json
import xlrd
from collections import OrderedDict
import xml.dom.minidom as minidom
import html

def xls2json(file_path):  
  data = xlrd.open_workbook(file_path)
  sheet = data.sheet_by_index(0)
  # use orderdict, make sure the correct position of element
  d = OrderedDict()
  for i in range(sheet.nrows):
    values = sheet.row_values(i) # map(): do the same operation for each element
    # d[values[0]] = values[1:]
    d[values[0]] = values[1]
  return d
  
class Make_xml(): # the parameter of class is for the base class
  def __init__(self,xml_path): # this parameter is the function parameter
    self.xml_path = xml_path
    self.dom = minidom.DOMImplementation().createDocument(None,'root',None) # dom is tree-like structure
    self.root = self.dom.documentElement
    
  def create_node(self, node_name, node_text=None, comment=None):
    if None == node_text:
      new_node = self.dom.createElement(node_name) # element is one type of node, which can contain another element node
    else:
      if None != comment:
        new_text = self.dom.createTextNode(comment+node_text) # textnode is another type of node, which is the final node
      else:
        new_text = self.dom.createTextNode(node_text)
      new_node = self.dom.createElement(node_name)
      new_node.appendChild(new_text)
    return new_node
    
  def add_child(self, item, comment=None):
    # attention chinese
    new_node = self.create_node('city', json.dumps(item,indent=4,\
                                                      ensure_ascii=False,\
                                                      separators=(',',':')),comment)
    self.root.appendChild(new_node)
    
  def save(self):
    with open(self.xml_path,'w') as f:
      transform = html.unescape(self.dom.toxml()) # html unescape, also has escape, meaning transforming form
      #transform = self.dom.toxml()
      f.write(transform)
      
      
if __name__ == '__main__':
  comment = '''
<!--
  城市信息
-->
'''
  xml_path = r'C:/Users/王宇树/Documents/wys/show-me-the-code/city.xml'    
  xls_path = r'C:/Users/王宇树/Documents/wys/show-me-the-code/city.xls'       
  new_xml = Make_xml(xml_path)
  new_xml.add_child(xls2json(xls_path),comment)
  new_xml.save()
    
    
