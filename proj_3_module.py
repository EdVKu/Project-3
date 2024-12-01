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
    sTop = lat[i+1,j]
    sBot = lat[i-1,j]
    sLeft = lat[i,j-1]
    sRight = lat[i,j+1]
    return sTop, sBot, sLeft, sRight
def flip(L, lat, temp, H = 0):

    a = rd.randint(0,L-2)
    b = rd.randint(0,L-2)
    Flip = 0
    
    mov = np.array(lattice(a,b,lat))
    delE = 2*lat[a,b]*(np.sum(mov)+H)
    if (delE <= 0) or (delE>0 and np.random.rand(1)[-1]< np.exp(-delE/temp)):
        Flip = -lat[a,b]
        lat[a,b] = Flip 
    return np.matrix(lat), Flip

def onsager(T,Tc):
  if T >=Tc:
    return 0
  else:
    return (1-np.sinh(2/T)**(-4))**(1/8)

def dele(L, lat, H = 0):
    a = rd.randint(0,L-2)
    b = rd.randint(0,L-2)
    # E[-1] + dele(L,lat0)
    mov = np.array(lattice(a,b,lat))

    return 2*lat[a,b]*(np.sum(mov)+H)
def energy(lat, L, H = 0):
    e = 0
    for i in range(L-1):
        for j in range(L-1):
            e -= (lat[i,j]*(np.sum(np.array(lattice(i,j,lat)))) + H*np.sum(lat))
    return e/2

def two_dim_ising(L, temp, H = 0, n = 200):
    lat = np.ones((L,L))
    E = [energy(lat, L, H)]
    Eq = [E[-1]**2]
    lat0 = lat
    S = [np.sum(lat)]
    Sq = [S[-1]**2]
    ons = S
    onsq = Sq
    one = E
    oneq = Eq
    for i in range(n):

        lat0, dels = flip(L, lat, temp, H)
        lat1 = lat0
        delen = dele(L,lat1)
        S.append(S[-1] + 2*dels)
        E.append(E[-1] + delen)
        Sq.append((Sq[-1]+2*dels)**2)
        Eq.append((Eq[-1]+delen)**2)
        eps = (np.mean(ons)*i + S[-1])/(i+1)
        epe = (np.mean(one)*i + E[-1])/(i+1)  
        epse = (np.mean(oneq)*i + Eq[-1])/(i+1)
        epss = (np.mean(onsq)*i + Sq[-1])/(i+1)
        ons.append(eps)
        one.append(epe)
        oneq.append(epse)
        onsq.append(epss)


    
    N = L**2
    U = 1/N*one[-1]
    xi_t = (onsq[-1]-ons[-1]**2)/((N*temp))
    M = 1/N*ons[-1]
    C_H = (oneq[-1]-one[-1]**2)/((N*temp**2))
    return lat1, U, M, n, n/N, xi_t, C_H





