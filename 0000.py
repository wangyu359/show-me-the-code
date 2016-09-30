# -*- coding: utf-8 -*-

"""

Created on Fri Sep 30 15:32:20 2016



@author: based on other's code in the internet

"""



from PIL import Image,ImageFont,ImageDraw#从PIL库导入所需模块



def stamp_num(img, num, write_path):

  drawSurface = ImageDraw.Draw(img)

  print(img.size)

  

  fontPath = r'C:/Windows/Fonts/calibri'

  numFont = ImageFont.truetype(fontPath,min(img.size)//40)

  

  # I do not quite get the idea of the first parameter in drawSurface.text

  drawSurface.text((img.size[0]-min(img.size)//40,0),num,fill=(255,0,0),font=numFont)

  img = img.resize((img.size[0],img.size[1]))

  img.save(write_path)

  img.show()





if __name__ == '__main__':

  read_path = r'C:/Users/王宇树/Documents/WIN.jpg'

  img = Image.open(read_path)

  write_path = r'C:/Users/王宇树/Documents/WIN_num.jpg'

  stamp_num(img,"999",write_path)
