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


def two_dim_ising(L, temp, n):
    return 0
probs = np.array([3,3,1,1,1,1])/10
earnings = np.array([1,1,-1,-1,-1,-1])

Y = [np.abs(probs @ earnings- np.mean(weighted_die(10**i))) for i in range(1,5)]
X = [i for i in range(1,5)]




