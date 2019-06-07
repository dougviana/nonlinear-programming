# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:37:06 2013

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 07 16:02:03 2013

@author: User
"""

from entrada import d, eps, f

#inicializacao de variavel
v_aux = []
for i in range(d):
    v_aux.insert(i, 0.0)


#busca linear por ajuste quadratico    
def bl(x, h, s): 
    
    #faz gl(lamb) = f(x + lamb*h)
    def gl(lamb):
        for i in range(d):
            v_aux[i] = x[i] + lamb*h[i]
        gl = f(v_aux)
        return gl
        
    #monta segmento [a---lamb---b]
    a = 0.0
    b = 2*s
    lamb = s
    
    #cercar lambda minimo
    if (gl(b) < gl(lamb)):
        while (gl(b) < gl(lamb)):
            a = lamb
            lamb = b
            b = 2*b
            
        #monta segmento [a---v---w---b]
        v = lamb
        w = 0.5*(lamb + b)
        
        #eliminina um subintervalo
        if (gl(v) <= gl(w)):
            lamb = v
            b = w
        else:
            a = v
            lamb = w
    
    #reduz intervalo [a---lamb---b] pela interpolacao
    if ((b - a) > eps):
        
        #interpolacao
        lamb_aux = lamb + ((gl(a) - gl(b)))/(2*(gl(a) - 2*gl(lamb) + gl(b)))
        
        #verificar se lamb_aux pertence a [a,b]
        if(lamb_aux <= a):
            lamb_aux = (a + lamb)/2
        elif(lamb_aux >= b):
            lamb_aux = (lamb + b)/2
            
        #monta segmento [avwb]    
        if(lamb_aux <= lamb):
            v =  lamb_aux
            w = lamb
        else:
            v = lamb
            w = lamb_aux
            
        #eliminina um subintervalo
        if (gl(v) <= gl(w)):
            lamb = v
            b = w
        else:
            a = v
            lamb = w
            
        #ajuste quadratico        
        while ((b - a) > eps):
            #impede que seja feita divisao por zero
            if(lamb_aux == lamb): return lamb
            
            #interpolacao
            lamb_aux = 0.5*((lamb**2 - b**2)*gl(a) + (b**2 - a**2)*gl(lamb) + 
            (a**2 - lamb**2)*gl(b))/((lamb - b)*gl(a) + (b - a)*gl(lamb) + 
            (a - lamb)*gl(b))
            
            #verificar se lamb_aux pertence a [a,b]
            if(lamb_aux <= a):
                lamb_aux = (a + lamb)/2    
                
            elif(lamb_aux >= b):
                lamb_aux = (lamb + b)/2
                
            #monta segmento [avwb]    
            if(lamb_aux <= lamb):
                v =  lamb_aux
                w = lamb
            else:
                v = lamb
                w = lamb_aux
                
            #eliminina um subintervalo
            if (gl(v) <= gl(w)):
                lamb = v
                b = w
            else:
                a = v
                lamb = w
    return lamb