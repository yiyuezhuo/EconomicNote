# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:36:12 2016

@author: yiyuezhuo
"""

import sympy
import random

from sympy import S, Eq, solve,Symbol

'''
y,c=S('y c'.split())
equations=[Eq(y,0.5*c+1),Eq(c,2+0.6*y)]
print(solve(equations))
'''

'''function argument'''

def cal(exog_bind,args_bind):
    for key,value in args_bind.items():
        exec('{}={}'.format(key,str(value)))
    for key,value in exog_bind.items():
        exec('{}={}'.format(key,str(value)))
        
    y,c,i,r,P,N,L1,L2,f,h,W=S('y,c,i,r,P,N,L1,L2,f,h,W'.split(','))
    N=Symbol('N')
    
    '''equations function hypothesis'''
    c_y_t=Eq(c,Ca+Cb*(y-t))
    i_r=Eq(i,ia-ib*r)
    L1_y=Eq(L1,L1a+L1b*y)
    L2_r=Eq(L2,L2a-L2b*r)
    f_N=Eq(f,fa+fb*N)
    h_N=Eq(h,ha-hb*N)
    f_h=Eq(f,h)
    
    #equs_hypo=[c_y_t,i_r,L1_y,L2_r,h_N,y_N_kbar]
    
    '''equations main'''
    y_=Eq(y,c+i+g)
    P_=Eq(P,M/(L1+L2))
    f_=Eq(f,W/P)
    y__=Eq(y,ya-yb*N*kbar)
    
    '''
    equs_master=[y_,P_,f_,y__]
    
    equations=equs_hypo+equs_master
    
    solve(equations)
    '''
    
    '''IS curve'''
    
    map_y_c_i=solve([c_y_t,y_,i_r],[y,c,i])
    
    '''LM curve'''
    
    map_y_L1_L2=solve([L1_y,L2_r,P_],[y,L1,L2])
    
    '''total demand curve'''
    
    map_y_r=solve([Eq(y,map_y_c_i[y]),Eq(y,map_y_L1_L2[y])],[y,r])
    
    map_y_c_i_={key:map_y_c_i[key].subs({r:map_y_r[r]}) for key in [y,c,i]}
    map_y_L1_L2_={key:map_y_L1_L2[key].subs({r:map_y_r[r]}) for key in [y,L1,L2]}
    
    map_y_c_i_L1_L2={}
    map_y_c_i_L1_L2.update(map_y_c_i_)
    map_y_c_i_L1_L2.update(map_y_L1_L2_)
    
    '''total supply curve'''
    
    map_y_W_N_f_h=solve([f_N,h_N,f_h,f_,y__],[y,W,N,f,h],dict=True)[0]
    
    '''do it!'''
    
    map_y_P_c_i_N_W_L1_L2_h_f=solve([Eq(eq[0],eq[1]) for eq in list(map_y_c_i_L1_L2.items())+list(map_y_W_N_f_h.items())])[0]
    
    rd={}
    for key in 'y_P_c_i_N_W_L1_L2_h_f'.split('_'):
        exec('rd["{}"]=map_y_P_c_i_N_W_L1_L2_h_f[{}]'.format(key,key))
    return rd

def test():
    args_bind={key:random.random() for key in 'Ca,Cb,ia,ib,L1a,L1b,L2a,L2b,fa,fb,ha,hb,ya,yb'.split(',')}
    exog_bind=dict(g=1,kbar=10,t=1,M=5,W=5)
    return cal(exog_bind,args_bind)
        
        

Ca,Cb,ia,ib,L1a,L1b,L2a,L2b=S('Ca,Cb,ia,ib,L1a,L1b,L2a,L2b'.split(','))
fa,fb,ha,hb,ya,yb=S('fa,fb,ha,hb,ya,yb'.split(','))



Ca,Cb,ia,ib,L1a,L1b,L2a,L2b=map(lambda x:random.random(),[Ca,Cb,ia,ib,L1a,L1b,L2a,L2b])
fa,fb,ha,hb,ya,yb=map(lambda x:random.random(),[fa,fb,ha,hb,ya,yb])



'''exog'''
g,kbar,t,M=S('g,kbar,t,M'.split(','))

g=1
kbar=10
t=1
M=5

cons=[Ca,Cb,ia,ib,L1a,L1b,L2a,L2b,Ca,Cb,ia,ib,L1a,L1b,L2a,L2b,fa,fb,ha,hb,ya,yb,g,kbar,t,M]


'''endog'''
y,c,i,r,P,N,L1,L2,f,h,W=S('y,c,i,r,P,N,L1,L2,f,h,W'.split(','))
N=Symbol('N')

'''equations function hypothesis'''
c_y_t=Eq(c,Ca+Cb*(y-t))
i_r=Eq(i,ia-ib*r)
L1_y=Eq(L1,L1a+L1b*y)
L2_r=Eq(L2,L2a-L2b*r)
f_N=Eq(f,fa+fb*N)
h_N=Eq(h,ha-hb*N)
f_h=Eq(f,h)
y_N_kbar=Eq(y,ya+yb*N*kbar)

#equs_hypo=[c_y_t,i_r,L1_y,L2_r,h_N,y_N_kbar]

'''equations main'''
y_=Eq(y,c+i+g)
P_=Eq(P,M/(L1+L2))
f_=Eq(f,W/P)
y__=Eq(y,ya-yb*N*kbar)

'''
equs_master=[y_,P_,f_,y__]

equations=equs_hypo+equs_master

solve(equations)
'''

'''IS curve'''

map_y_c_i=solve([c_y_t,y_,i_r],[y,c,i])

'''LM curve'''

map_y_L1_L2=solve([L1_y,L2_r,P_],[y,L1,L2])

'''total demand curve'''

map_y_r=solve([Eq(y,map_y_c_i[y]),Eq(y,map_y_L1_L2[y])],[y,r])

map_y_c_i_={key:map_y_c_i[key].subs({r:map_y_r[r]}) for key in [y,c,i]}
map_y_L1_L2_={key:map_y_L1_L2[key].subs({r:map_y_r[r]}) for key in [y,L1,L2]}

map_y_c_i_L1_L2={}
map_y_c_i_L1_L2.update(map_y_c_i_)
map_y_c_i_L1_L2.update(map_y_L1_L2_)

'''total supply curve'''

map_y_W_N_f_h=solve([f_N,h_N,f_h,f_,y__],[y,W,N,f,h],dict=True)[0]

'''do it!'''

map_y_P_c_i_N_W_L1_L2_h_f=solve([Eq(eq[0],eq[1]) for eq in list(map_y_c_i_L1_L2.items())+list(map_y_W_N_f_h.items())])[0]
'''
map_y_P=solve([Eq(y,map_y_W_N_f_h[y]),Eq(y,map_y_c_i_L1_L2[y])],[y,P],dict=True)[0]

map_y_P_c_i_N_W_L1_L2_h_f={}
map_y_P_c_i_N_W_L1_L2_h_f.update(map_y_P)
#map_y_P_c_i_N_W_L1_L2_h_f[c]=map_y_c_i_L1_L2[c].subs(map_y_P)
map_y_P_c_i_N_W_L1_L2_h_f.update({key:map_y_c_i_L1_L2[key].subs(map_y_P) for key in [c,i,L1,L2]})
map_y_P_c_i_N_W_L1_L2_h_f.update({key:map_y_W_N_f_h[key].subs(map_y_P) for key in [W,N,f,h]})

'''