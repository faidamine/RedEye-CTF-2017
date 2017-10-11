from PIL import Image
from sys import stdout

img = Image.open('output.png')
img = img.convert("RGB")

pix = img.load()
x_size, y_size = img.size[0], img.size[1]
s = 89
def parse_pixels():
 
  for y in range(y_size):
    for x in range(x_size):
      stdout.write( chr(pix[x,y][0]^int(s)%256) + chr(pix[x,y][1]) + chr(pix[x,y][2]) )

parse_pixels();
