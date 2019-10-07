# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:43:38 2019

@author: raveaux
"""

import numpy as np
import matplotlib.pyplot as plt

def faircoin(n_xp):
  x=np.random.randint(low=0,high=2,size=n_xp)
  #np.random.binomial(1,0.5,(n_xp,1))
  return x


def fairdice(n_xp):
  x=np.random.randint(low=0,high=6,size=n_xp)
  #np.random.binomial(6,0.5,(n_xp,1))
  return x

def Pr(x):
    n_cases=np.unique(x).shape[0]
    #print(n_cases)
    res=np.zeros((n_cases))
    #print(res)
    for i in x:
        #print(i)
        res[i]=res[i]+1
    #for i in range(len(res)):
    #    res[i]/=float(len(x))
    res/=float(len(x))
    return res


def PrJoint(x,y):
    n_cases_x=np.unique(x).shape[0]
    n_cases_y=np.unique(y).shape[0]
    #print(n_cases)
    res=np.zeros((n_cases_x,n_cases_y))
    #print(res)
    for i in x:
        for j in y:
            res[i,j]=res[i,j]+1
            
    #for i in range(res.shape[0]):
    #    for j in range(res.shape[1]):
    res/=float(len(x)*len(y))
    return res

def PrCond(pxy,ystar):
    #pxy=PrJoint(x,y)
    pxystar= pxy[:,ystar]
    pystar=pxy[:,ystar].sum()
    res = pxystar/pystar
    return res


def Prxgiveny(pxy):
    #pxy=PrJoint(x,y)
    res = np.zeros((pxy.shape[0],pxy.shape[1]))
    for ystar in range(pxy.shape[1]):
        pxystar= pxy[:,ystar]
        pystar=pxy[:,ystar].sum()
        res[:,ystar] = pxystar/pystar
    return res


def Prxstargiveny(pxy,xstar):
    #pxy=PrJoint(x,y)
    res = np.zeros((1,pxy.shape[1]))
    for ystar in range(pxy.shape[1]):
        pxystar= pxy[xstar,ystar]
        pystar=pxy[:,ystar].sum()
        res[0,ystar] = pxystar/pystar
    return res


def Prygivenx(pxy):
    #pxy=PrJoint(x,y)
    res = np.zeros((pxy.shape[0],pxy.shape[1]))
    for xstar in range(pxy.shape[0]):
        pxstary= pxy[xstar,:]
        pxstar=pxy[xstar,:].sum()
        res[xstar,:] = pxstary/pxstar
    return res


def PrMarginalization(pxy):
    px=np.zeros((pxy.shape[0]))
    for index in range(pxy.shape[1]):
        px+=pxy[:,index]
    return px


def PrygivenxBayesRule(x,y,xstar):
    pxy=PrJoint(x,y)
    px=Pr(x)
    py=Pr(y)
    pxgiveny=Prxstargiveny(pxy,xstar)
    num=np.multiply(pxgiveny,py.T)
    #print("--------------------")
    #print(py)
    #print(pxy[xstar])
    #print(pxgiveny)
    #print(num)
   # print(px[xstar])
   # print(num/px[xstar])
   # input()
   # print("--------------------")
    return num/px[xstar]
    


lambd=0.8
x=np.random.binomial(1,lambd,(100,1))
plt.figure(1)
plt.hist(x)

lambd=0.8
y=np.random.binomial(1,lambd,(100,1))
plt.figure(2)
plt.hist(y)

plt.figure(3)
plt.hist2d(x[:,0],y[:,0])



xn=np.random.normal(0,1,(10000,1))
plt.figure(4)
plt.hist(xn)

yn=np.random.normal(0,1,(10000,1))
plt.figure(5)
plt.hist(yn)

plt.figure(6)
plt.hist2d(xn[:,0],yn[:,0])

plt.figure(7)

aa=np.where(xn[:,0]==0.0)
print(aa[0])


x=faircoin(100)
y=fairdice(100)
px=Pr(x)
py=Pr(y)
print(x.shape)
print(y.shape)
print(px.sum())
print(py.sum())
print(px.shape)
print(py.shape)

pxy=PrJoint(x,y)
print(pxy.sum())
print(pxy.shape)

pxgiveny5=PrCond(pxy,5)
print(pxgiveny5.shape)
pxgiveny0=PrCond(pxy,0)

print(pxgiveny5.sum())
print(pxgiveny0.sum())

pyx=PrJoint(y,x)
pygivenx0=PrCond(pyx,0)
print(pygivenx0.shape)
pygivenx1=PrCond(pyx,1)

print(pygivenx0.sum())
print(pygivenx1.sum())


pxx=PrMarginalization(pxy)
print(pxx.shape)
pyy=PrMarginalization(pyx)


pxgiveny=Prxgiveny(pxy)
print(pxgiveny)
print(pxgiveny.shape)
pygivenx=Prygivenx(pxy)
print(pygivenx)

pxstargiveny=Prxstargiveny(pxy,0)

print(pxstargiveny)
print(pxstargiveny.shape)


pvayes=PrygivenxBayesRule(x,y,1)
print(pvayes)
print(pvayes.shape)


plt.figure(8)
plt.hist(x)
plt.figure(9)
plt.hist(y)
plt.figure(10)
plt.plot(px,'ro')
plt.figure(11)
plt.plot(py,'ro')

plt.figure(12)
plt.imshow(pxy)
plt.close()
plt.figure(13)
plt.matshow(pxy)
plt.close()
plt.figure(14)
plt.plot(pxgiveny5,'ro')
plt.figure(15)
plt.plot(pxgiveny0,'ro')
plt.figure(16)
plt.plot(pygivenx0,'ro')
plt.figure(17)
plt.plot(pygivenx1,'ro')
plt.figure(18)
plt.plot(px,'ro')
plt.figure(19)
plt.plot(pxx,'ro')
plt.figure(20)
plt.plot(py,'ro')
plt.figure(21)
plt.plot(pyy,'ro')



#plt.hist(yn[xn[:,0]==0],0)
#b=np.random.normal(0,1,(100,1))
#plt.figure(2)
#plt.hist(b)


#c=np.random.normal(0,1,(100,1))
#plt.figure(3)
#plt.plot(b,c,'ro')
#plt.hist2d(b,c)
