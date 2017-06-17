# -*- coding: utf-8 -*-
from md5 import md5
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

s = openread(spath)

es = md5(s).hexdigest()
openwrite(es,espath)

formatt = '''
       明文:"%s"
        md5:"%s"
'''
print formatt%(s,es)
