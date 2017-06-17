# -*- coding: utf-8 -*-
def openread(path):
    with open(path,'r') as f:
        strr = f.read()
    return strr
def openwrite(strr,path,mode='w'):
    with open(path,mode) as f:
        f.write(strr)
    return path
from pyDes import *
from binascii import b2a_hex, a2b_hex

spath = './s.txt'
espath = './es.txt'

KEY = "KEYKEYKE"    #密钥
IV = "IVIVIVIV"     #偏转向量
# 使用DES对称加密算法的CBC模式加密
k = des(KEY, CBC, IV, pad=None, padmode=PAD_PKCS5)

s = openread(spath)
es = k.encrypt(s)
es_ = b2a_hex(es) # 2进制转换为16进制

openwrite(es_,espath)

es = a2b_hex(openread(espath))  # 读取16进制转换为2进制
ds =  k.decrypt(es)
formatt = '''
       明文:"%s"
       密匙:"%s"
    偏转向量:"%s"
加密后的密文:"%s"
解密后的结果:"%s"
'''
print formatt%(s,KEY,IV,es_,ds)


    
