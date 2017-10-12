#!/usr/bin/env python3
import base64
import gmpy2
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open('id_rsa.pub') as fh:
    key = RSA.importKey(fh.read())

s = bin(key.n)[2:]
a = s.find('0') + 1
b = len(s) - a
assert a < b
assert s == ('1' * (a-1) + '0' + '1' * (b-a) + '0' * (a-1) + '1')
p = 2**a-1
q = 2**b-1
assert p * q == key.n

d = lambda p, q, e: int(gmpy2.invert(e, (p-1)*(q-1)))
key = RSA.construct((p*q, key.e, d(p, q, key.e)))
key = PKCS1_OAEP.new(key)
with open('flag.enc') as fh:
    c = base64.b64decode(fh.read())
print(key.decrypt(c).decode())
