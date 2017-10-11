from PIL import Image

data = ""
d = open("pwwww").read().split("\n")
del d[-1]
s = 89
for i in range( 256**2 ):
  for x in d:
      data += chr(int(x)^int(s)%256) + chr(0) + chr(0)
im = Image.fromstring("RGB", (256,256), data)
im.save("output.png", "PNG")
