# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 17:26:12 2016

@author: wys
"""

import code_0001_others_unicity
import pymysql

def put_sqldb(num,length=10):  
  try:
    conn=pymysql.connect(user='root') # conn=MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306)
    cur=conn.cursor()
    
    cur.execute('create database if not exists 0002_db')
    conn.select_db('0002_db')
    cur.execute('create table code1(id int,activation_code varchar(%s))',length)
  
    for id in range(num):
      value = code_0001_others_unicity.activation_code(id,length)
      cur.execute('insert into code1 values(%s,%s)',(id ,value))    
      
    conn.commit()
    cur.close()
    conn.close()
    
  except pymysql.Error:
    print('mysql error!!!!!!')

if __name__=='__main__':
  put_sqldb(20)
