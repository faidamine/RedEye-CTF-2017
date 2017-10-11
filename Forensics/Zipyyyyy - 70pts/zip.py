import commands
import os

i = 222
while i > 0:
    res = commands.getstatusoutput('fcrackzip -v -D -u -p  rockyou.txt zipy_'+str(i)+'.zip > res')
    text=open('res')
    passw=str(text.read().split('== ')[1]).strip()
    cmd = "unzip -P %s %s"%(str(passw),'zipy_'+str(i)+'.zip')
    print cmd
    os.system(cmd)
    i -= 1
