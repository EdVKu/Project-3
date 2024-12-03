import numpy as np
import random as rd
import matplotlib.pyplot as plt
def prop(d,b):
    if np.random.normal(b,1,100)[0]-b<0:
        return d[int((b)%6)-2]
    else:
        return d[int((b)%6)]

def weighted_die(n):
    probs = np.array([3,3,1,1,1,1])/10
    earnings = np.array([1,1,-1,-1,-1,-1])
    dice = [1,2,3,4,5,6]
    d0 = dice[:]
    rd.shuffle(dice)
    sigma = dice[0]
    samp = []
    for i in range(n+1):
        sigmap = prop(d0,sigma)
        
        if 1<=sigma<=2 and 1<=sigmap<=2:
            f, fp = 3, 3
        elif 2<sigma and 1<=sigmap<=2:
            f, fp = 1, 3
        elif 2<sigmap and 1<=sigma<=2:
            f, fp = 3, 1
        else:
            f, fp = 1, 1
        alpha = fp/f
        if rd.randrange(100000000)/100000000 <= alpha:
            samp.append(sigmap)
            sigma = sigmap
        else:
            samp.append(sigma)

    gain = []  
    for i in samp:
        if i>2:
            gain.append(-1)
        else:
            gain.append(1)
    
    return gain

def lattice(i,j,lat):
    L, H = lat.shape
    
    sTop = lat[int((i+1)%(L)),j]
    sBot = lat[int((i-1)%(L)),j]
    sLeft = lat[i,int((j-1)%(L))]
    sRight = lat[i,int((j+1)%(L))]
    return int(sTop), int(sBot), int(sLeft), int(sRight)

def flip(L, lat, temp, H = 0):
    Flp = 0
    for i in range(L):
        for j in range(L):
            a = rd.randint(0,L-1)
            b = rd.randint(0,L-1)
            Ss = lat[a,b]
            costo = lat[(a+1)%L,b] + lat[(a-1)%L,b] + lat[a,(b+1)%L] + lat[a,(b-1)%L]
            delE = 2*Ss*costo
            if delE <= 0:
                Ss *= -1
            elif (delE >0 and np.random.rand(1)[0]<np.exp(-delE/temp)):
                Ss *= -1
            lat[a,b] = Ss
    Flp = Ss
    return lat, Flp, delE


def onsager(T,Tc):
  if T >=Tc:
    return 0
  else:
    return (1-np.sinh(2/T)**(-4))**(1/8)

def energy(lat, L, H = 0):
    e = 0
    for i in range(L-1):
        for j in range(L-1):
            Ss = lat[i,j]
            costo = lat[(i+1)%L,j] + lat[(i-1)%L,j] + lat[i,(j+1)%L] + lat[i,(j-1)%L]
            e -= (Ss*(costo))
            
    return e/4
def sspin(lat):
    mag = np.sum(lat)
    return mag

def two_dim_ising(L, temp, H = 0, n = 200):
    lat = np.ones((L,L))    
    E = [energy(lat, L, H)]
    Eq = [E[-1]**2]
    S = [np.sum(lat)]
    Sq = [S[-1]**2]
    emean = np.mean(E)
    smean = np.mean(S)
    Sqmean = np.mean(Sq)
    Eqmean = np.mean(Eq)
    ons, onsq, one, oneq = 0,0,0,0
    for i in range(n):
        lat, dels, delen = flip(L, lat, temp, H)
        ons = np.sum(lat)
        onsq = ons**2
        one = energy(lat, L, H)
        oneq = one**2
        S.append(ons)
        E.append(one)
        Sq.append(onsq)
        Eq.append(oneq)
        eps = (smean * i + ons)/(i+1)
        epe = (emean * i + one)/(i+1)  
        epse = (Eqmean * i + oneq)/(i+1)
        epss = (Sqmean * i + onsq)/(i+1)
        smean, emean, Eqmean, Sqmean = eps, epe, epse, epss



    N = L**2
    U = 1/N*epe
    xi_t = (epss-eps**2)/((N*temp))
    M = 1/N*eps
    C_H = (epse-epe**2)/((N*temp**2))
    
        


    return lat, U, M, xi_t, C_H


    
"""
    
    
    lat0 = lat
    
    

    delen = dele(L,lat)
    
    
    
    
    eps = (np.mean(ons) * i + S[-1])/(i+1)
    epe = (np.mean(one) * i + E[-1])/(i+1)  
    epse = (np.mean(oneq) * i + Eq[-1])/(i+1)
    epss = (np.mean(onsq) * i + Sq[-1])/(i+1)
    ons.append(eps)
    one.append(epe)
    oneq.append(epse)
    onsq.append(epss)

"""
    



