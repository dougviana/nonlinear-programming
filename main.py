# -*- coding: utf-8 -*-

from entrada import d, eps, x, f, g
from busca_linear import bl
from norma import norma

#inicializacao de variaveis    
k = 0   #contador
j = 0   #contador
lamb = 1.0  #lambda inicial
xj=[]   #vetor utilizado no metodo gradiente
xk=[]   #vetor utilizado no metodo partan
hj = [] #direcao utilizada no metodo gradiente
hk = [] #direcao utilizada no metodo partan

#zera vetores criados
for i in range(d):
    xj.insert(i, 0.0)
    xk.insert(i, 0.0)
    hj.insert(i, 0.0)
    hk.insert(i, 0.0)

#atribui x, (vetor inicial), a xj e xk
xj = [i for i in x]
xk = [i for i in x]


#duas iteracoes do metodo gradiente
while ((norma(xj) >= eps) and (j < 2)):
    gj = g(xj)
    hj = [-1.0*i for i in gj]
    
    #encontra o melhor lambda em relacao a xj e hj
    lamb = bl(xj, hj, lamb)    
    #busca na direcao hj determinando x_(j+1)
    for i in range(d):
        xj[i] = xj[i] + lamb*hj[i] 
    j = j + 1
    
#metodo partan = (passo de aceleracao + passo de gradiente)
if (norma(xj) >= eps):
    #primeiro passo de aceleracao    
    k = 1
    yk = xj
    for i in range(d):
        hk[i] = yk[i] - xk[i]
    
    #encontra o melhor lambda em relacao a yk e hk
    lamb = bl(yk, hk, lamb)
    #busca na direcao hk, a partir de yk, determinando x_(k+1)
    for i in range(d):
        xk[i] = yk[i] + lamb*hk[i]
        
    #passo de gradiente seguido de um passo de aceleracao
    while(norma(xk) >= eps):
        gk = g(xk)
        hk = [-1.0*i for i in gk]
        
        #encontra o melhor lambda em relacao a xk e hk
        lamb = bl(xk, hk, lamb)
        #busca na direcao h_(k+1), a partir de x_(k+1), determinando y_(k+1)
        for i in range(d):
            yk[i] = xk[i] + lamb*hk[i]
            
        #atualizacao do contador e da direcao hk            
        k = k + 1
        for i in range(d):
            hk[i] = yk[i] - xk[i]
        
        #encontra o melhor lambda em relacao a xj e hj
        lamb = bl(yk, hk, lamb)
        #busca na direcao hk, a partir de yk, determinando x_(k+1)
        for i in range(d):
            xk[i] = yk[i] + lamb*hk[i]

arquivo = file("saida.txt", "w")
arquivo.write(str(f(xk)))
arquivo.write("\n")
arquivo.write(str(xk))
arquivo.close()
