# -*- coding: utf-8 -*-
from math import log
def openread(path):
    with open(path,'r') as f:
        strr = f.read()
    return strr
def openwrite(strr,path,mode='w'):
    with open(path,mode) as f:
        f.write(strr)
    return path

def primeNumbers(maxx=100): # 获得小于maxx的所有质数
    l = [2,3]
    b = 4
    while 1:  
        for i in l:
            if b%i ==0:
                break
        else:
            l += [b]
        b += 1
        if b > maxx:
            break
    return l

def gcde(fn):
    '''
    找到第一个与fn互素的质数
    '''
    l = primeNumbers(fn**0.5)
    for i in l:
        if fn%i:
            return i
    else:
        raise Exception,'没有合适的e, 请把p, q设置大一点'

intToHex = lambda n,b=2:('0'*b+(hex(int(n))[2:]))[-b:]
class PubKey():
    def __init__(self,e,n):
        self.e,self.n = e,n
    def _encodeInt(self,intt):
        return intt**self.e%self.n
    def encode(self,s):
        n = self.n
        if isinstance(s,int):
            return self._encodeInt(s)
        maxn = int(log(n,16))
        rawhexs = (''.join([intToHex(ord(c),2) for c in s]))
        zeros = (maxn - (len(rawhexs)%maxn))%maxn
        hexs = intToHex(zeros,maxn)+'0'*zeros+rawhexs
        hexss = [''.join(t) for t in zip(*[hexs[i::maxn] for i in range(maxn)])]
        ints = [int('0x'+h,16) for h in hexss]
        eints = map(self._encodeInt,ints)
        es = ''.join([intToHex(i,maxn+1) for i in eints])
#        print maxn,zeros,rawhexs,hexss,eints,s
        return es
        
    def __str__(self):
        return 'PubKey:e = %d, n = %d'%(self.e,self.n)
    __repr__ = __str__
class PriKey():
    def __init__(self,d,n,p,q,fn):
        self.d,self.n = d,n
        self.p,self.q = p,q
        self.fn = fn
    def _decodeInt(self,intt):
        return intt**self.d%self.n
    def decode(self,es):
        if isinstance(es,int):
            return self._decodeInt(es)
        n = self.n
        maxn = int(log(n,16))
        ess = [''.join(t) for t in zip(*[es[i::maxn+1] for i in range(maxn+1)])]
        eints = [int('0x'+(h),16) for h in ess]
        ints = map(self._decodeInt,eints)
        zeros = ints[0]
        hexs = [intToHex(i,maxn) for i in ints[1:]]
        rawhexs = ''.join(hexs)[zeros:]
        ds = ''.join([chr(int('0x'+i[0]+i[1],16)) for i in zip(rawhexs[::2],rawhexs[1::2])])
#        print maxn,zeros,rawhexs,eints,ds
        return ds
    def __str__(self):
        return 'PriKey:d = %d, n = %d, p = %d, q = %d, fn = %d'%\
        (self.d,self.n,self.p,self.q,self.fn)
    __repr__ = __str__

def createKeyByPQ(p=11,q=17):
    n = p*q
    fn = (p-1)*(q-1)
    e = gcde(fn)
#    e = 7
    tmp = 1
    '''找d'''
    while 1: 
        tmp += fn
        if tmp%e ==0:
            d = tmp//e
            break
        if tmp > fn*e:
            raise Exception,'没有合适的b, 请把p, q设置大一点'
            break
    pub = PubKey(e,n)
    pri = PriKey(d,n,p,q,fn)
    return pri,pub
def randomCreateKey(bit=10):
    '''
    根据位数bit 来生成keys
    '''
    minn,maxx = 2**(bit/2),2**(bit+1)/2
    l = primeNumbers(maxx)
    filter(lambda x:x>minn,l)
    print len(l)
    import random
    p = random.choice(l)
    l.remove(p)
    q = random.choice(l)
    return createKeyByPQ(p,q)
if __name__ == '__main__':
    spath = './s.txt'
    espath = './es.txt'
    pri,pub = randomCreateKey(bit=10)
    
    s = openread(spath)    
    es=pub.encode(s)
    openwrite(es,espath)
    ds=pri.decode(es)
    
    formatt = '''
       明文:"%s"
       公钥:"%s"
       密钥:"%s"
加密后的密文:"%s"
解密后的结果:"%s"
'''
    print formatt%(s,str(pub),str(pri),es,ds)

    
    
    
    
def test():
    pub = PubKey(e,n)
    pri = PriKey(d,n,p,q,fn)
    #n = 16**3
    s = 'aaaa'
    maxn = int(log(n,16))
    #maxn = 3
    intToHex = lambda n,b=2:('0'*b+(hex(int(n))[2:]))[-b:]
    rawhexs = (''.join([intToHex(ord(c),2) for c in s]))
    
    zeros = (maxn - (len(rawhexs)%maxn))%maxn
    
    hexs = intToHex(zeros,maxn)+'0'*zeros+rawhexs
    
    hexss = [''.join(t) for t in zip(*[hexs[i::maxn] for i in range(maxn)])]
    ints = [int('0x'+h,16) for h in hexss]
    self=pub
    eints = map(self._encodeInt,ints)
    es = ''.join([intToHex(i,maxn+1) for i in eints])
    print maxn,zeros,rawhexs,hexss,eints,s
    self=pri
    maxn = int(log(n,16))
    ess = [''.join(t) for t in zip(*[es[i::maxn+1] for i in range(maxn+1)])]
    eints = [int('0x'+(h),16) for h in ess]
    ints = map(self._decodeInt,eints)
    zeros = ints[0]
    hexs = [intToHex(i,maxn) for i in ints[1:]]
    rawhexs = ''.join(hexs)[zeros:]
    ds = ''.join([chr(int('0x'+i[0]+i[1],16)) for i in zip(rawhexs[::2],rawhexs[1::2])])
    print maxn,zeros,rawhexs,hexss,eints,ds
    
    intt = 88
    ei = pub._encodeInt(intt)
    
    print intt,ei,pri._decodeInt(ei)




