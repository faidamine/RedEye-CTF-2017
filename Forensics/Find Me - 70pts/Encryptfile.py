from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, sys, pkg_resources
 
def encrypt(key, filename):
        chunksize = 64 * 1024
        outFile = os.path.join(os.path.dirname(filename), "(encrypted)"+os.path.basename(filename))
        filesize = str(os.path.getsize(filename)).zfill(16)
        IV = ''
 
        for i in range(16):
                IV += chr(random.randint(0, 0xFF))
       
        encryptor = AES.new(key, AES.MODE_CBC, IV)
 
        with open(filename, "rb") as infile:
                with open(outFile, "wb") as outfile:
                        outfile.write(filesize)
                        outfile.write(IV)
                        while True:
                                chunk = infile.read(chunksize)
                               
                                if len(chunk) == 0:
                                        break
 
                                elif len(chunk) % 16 !=0:
                                        chunk += ' ' *  (16 - (len(chunk) % 16))
 
                                outfile.write(encryptor.encrypt(chunk))

 
def main():
       
        password = raw_input("Enter the password: ")
        encFiles = raw_input("Enter your file : ")
        encrypt(SHA256.new(password).digest(), str(encFiles))
        print "Done encrypting %s" %str(encFiles)
                                
 
main()
