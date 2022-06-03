import numpy as np
import os
from numba import njit, prange, jit

@jit
def convolucaoNumba (E, ImArray, rows, cols, janela, opcao):
    for row in prange(rows):
        for col in prange(cols):
            Lx=max(0,col-janela)
            Ux=min(cols,col+janela+1)
            Ly=max(0,row-janela)
            Uy=min(rows,row+janela+1)
            mascara=ImArray[Ly:Uy,Lx:Ux].flatten()
            He=0.0
            lenVet=mascara.size
            Lista=list(set(mascara))
            if len(Lista)==1 and Lista.count(0)==1:
                E[row,col]=0
            else:

                    prob=[(mascara[mascara==i]).size/(lenVet*1.0) for i in Lista]
                    for p in prob:
                        if p>0:
                            He += -1.0*p*np.log2(p)
                    if opcao==0:
                        E[row,col]=He

                    N=len(Lista)*1.0
                    if N == 1:
                        C=0
                    else:
                        Hmax=np.log2(N)
                        C=He/Hmax
                    if opcao==1:
                        E[row,col]=C
                    if opcao==2:
                        SDL=(1-C)*C
                        E[row,col]=SDL
                    if opcao==3:
                        D = 0.0
                        for p in prob:
                            D += (p-(1/N))**2
                        LMC=D*C
                        E[row,col]=LMC

    return E