# -*- coding: utf-8 -*-
def openread(path):
    with open(path,'r') as f:
        strr = f.read()
    return strr
def openwrite(strr,path,mode='w'):
    with open(path,mode) as f:
        f.write(strr)
    return path
spath = './s.txt'
espath = './es.txt'

import random
from md5 import md5
from Crypto.PublicKey import DSA

pri = DSA.generate(1024)
pub = pri.publickey()

s = openread(spath)
h = md5(s).hexdigest()

k = random.randint(2, pub.q-1)
sig = pri.sign(h, k)
openwrite(str(sig),espath)

_h = md5(openread(spath)).hexdigest()
_sig = eval(openread(espath))
r = "文档未被改变" if pub.verify(_h, _sig) else "文档验证错误"
formatt = '''
       明文:"%s"
       签名:"%s"
     (s, r):"%s"
    验证结果:"%s"
'''
print formatt%(s,_h,str(_sig),r)




