from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, sys, pkg_resources
 

def decrypt(key, filename):
        outFile = os.path.join(os.path.dirname(filename), os.path.basename(filename[11:]))
        chunksize = 64 * 1024
        with open(filename, "rb") as infile:
                filesize = infile.read(16)
                IV = infile.read(16)
 
                decryptor = AES.new(key, AES.MODE_CBC, IV)
               
                with open(outFile, "wb") as outfile:
                        while True:
                                chunk = infile.read(chunksize)
                                if len(chunk) == 0:
                                        break
 
                                outfile.write(decryptor.decrypt(chunk))
 
                        outfile.truncate(int(filesize))

def main():
       
        decrypt(SHA256.new("blackhat#99").digest(), "(encrypted)flag.png")
        print "Done decrypting %s" %filename
        os.remove(filename)
                                
 
main()



                
