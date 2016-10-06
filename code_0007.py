# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:11:06 2016

@author: wys
"""

import os

def code_line(code_file_path):
  code, blank, note = 0, 0, 0
  for root, dirs, files in os.walk(code_file_path):
    for item in files:
      file_abs_path = os.path.join(root,item)
      postfix = os.path.splitext(file_abs_path)[1]
      if postfix == '.py':
        with open(file_abs_path,encoding='utf8') as fp:
          while True:
            l = fp.readline()
            if not l:
              print('break')
              break
            elif l.strip().startswith('#'): # delete blank character, including '\n', '\r', '\t', ''
              note += 1
            elif l.strip().startswith('"""') or l.strip().startswith("'''"):
              note += 1
              if l.count('"""') == 1 or l.count("'''") == 1:
                while True:
                  l = fp.readline()
                  note += 1
                  if ("'''" in l) or ('"""' in l):
                    break
            elif l.strip():
              code += 1
            else:
              blank += 1
  return code, blank, note
  
  
if __name__ == '__main__':
  code_file_path = r'd:/show-me-the-code/0006/'
  code,blank, note = code_line(code_file_path)
  print('code:',code,'blank:',blank,'note:',note)
