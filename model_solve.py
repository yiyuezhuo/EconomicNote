# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:36:12 2016

@author: yiyuezhuo
"""

import sympy

from sympy import S, Eq, solve,Symbol

'''
y,c=S('y c'.split())
equations=[Eq(y,0.5*c+1),Eq(c,2+0.6*y)]
print(solve(equations))
'''

'''function argument'''

Ca,Cb,ia,ib,L1a,L1b,L2a,L2b=S('Ca,Cb,ia,ib,L1a,L1b,L2a,L2b'.split(','))
fa,fb,ha,hb,ya,yb=S('fa,fb,ha,hb,ya,yb'.split(','))

Ca,Cb,ia,ib,L1a,L1b,L2a,L2b=map(lambda x:0.5,[Ca,Cb,ia,ib,L1a,L1b,L2a,L2b])
fa,fb,ha,hb,ya,yb=map(lambda x:0.5,[fa,fb,ha,hb,ya,yb])

'''exog'''
g,kbar,t,M,W=S('g,kbar,t,M,W'.split(','))

g=1
kabr=10
t=1
M=5
W=5

'''endog'''
y,c,i,r,P,N,L1,L2,f,h=S('y,c,i,r,P,N,L1,L2,f,h'.split(','))

'''equations function hypothesis'''
c_y_t=Eq(c,Ca+Cb*(y-t))
i_r=Eq(i,ia-ib*r)
L1_y=Eq(L1,L1a+L1b*y)
L2_r=Eq(L2,L2a-L2b*r)
#f_N=Eq(f,fa+fb*N)
h_N=Eq(h,ha-hb*N)
y_N_kbar=Eq(y,ya+yb*N*kbar)

equs_hypo=[c_y_t,i_r,L1_y,L2_r,h_N,y_N_kbar]

'''equations main'''
y_=Eq(y,c+i+g)
P_=Eq(P,M/(L1+L2))
f_=Eq(f,W/P)
y__=Eq(y,ya-yb*N*kbar)

equs_master=[y_,P_,f_,y__]

equations=equs_hypo+equs_master

solve(equations)