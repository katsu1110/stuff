# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:05:53 2018

@author: katsuhisa
"""

#%%
# Q1
a = str(input())

if a[0:3]=='yah' and a[3]==a[4]:
    print('YES')
else:
    print('NO')

#%%    
# Q2
X, K = map(int, input().split())
Yx = X + 1
Yk = '1'
for k in range(K):
    Yk += '0'
Yk = int(Yk)
if Yk < Yx:
    b = Yk
    while Yk < Yx:
        Yk += b
    
print(str(Yk))
   
#%% 
# Q3
for i in range(4):
    if i==0:
        N = int(input())
    elif i==1:
        x = list(map(int, input().split()))
    elif i==2:
        c = list(map(int, input().split()))
    elif i==3:
        v = list(map(int, input().split()))

shojikin = 0
def baikyaku(x,c,v,shojikin):
    shojikin += x[0]
    x = x[1:]
    rat = [a/b for a,b in zip(v,c)]
    idx = v.index(max(rat))
    v.pop(idx)
    c.pop(idx)
    
    return x,c,v,shojikin

def kounyu(c,v,shojikin):
    def bestvalue(i,c,v,shojikin):
        if i==0: return 0
        if c[i-1] > shojikin:
            return bestvalue(i-1,c,v,shojikin)
        else:
            return max(bestvalue(i-1,c,v,shojikin),
                       bestvalue(i-1,c,v,shojikin-c[i-1]) + v[i-1])

    return bestvalue(len(c),c,v,shojikin)
 
value = 0
for n in range(N,1,-1):
    try:
        for i in range(n):
            x,c,v,shojikin = baikyaku(x,c,v,shojikin)
        val = kounyu(c,v,shojikin)
        if val > value:
            value = val
    except:
        continue    

print(value)
