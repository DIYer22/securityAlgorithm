# -*- coding: utf-8 -*-
def openread(path):
    with open(path,'r') as f:
        strr = f.read()
    return strr
def openwrite(strr,path,mode='w'):
    with open(path,mode) as f:
        f.write(strr)
    return path

def encodeVigenere(s, step):
    return ''.join([chr((ord(c)+step)%256) for c in s])

def decodeVigenere(s, step):
    return ''.join([chr((ord(c)-step)%256) for c in s])

spath = './s.txt'
espath = './es.txt'

s = openread(spath)
step = 3

es = encodeVigenere(s,step)
openwrite(es,espath)
ds = decodeVigenere(es,step)

formatt = '''
       明文:"%s"
       密匙:"%s"
加密后的密文:"%s"
解密后的结果:"%s"
'''
print formatt%(s,step,es,ds)




