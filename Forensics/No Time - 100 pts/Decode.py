import qrtools
import glob

l = []
for filed in glob.glob('./*.png'):
    qr = qrtools.QR()
    if qr.decode(filed):
         print('result: ' + qr.data)
         if (qr.data).startswith("http"):
             l.append(qr.data)
         else:
             pass
             
    else:
         print('error: ')
    
