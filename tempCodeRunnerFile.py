        S.append(S[-1] + lat[a,b])
        E.append(E[-1] + delE)
        Sq.append(((-Sq[-1]+(2*(lat[a,b]))**2)))
        Eq.append(((-Eq[-1]+delE**2)))
        eps = (np.mean(ons) * i + S[-1]) / (i + 1)
        epe = (np.mean(one) * i + E[-1]) / (i + 1)
        epse = (np.mean(oneq) * i + Eq[-1])/(i+1)
        epss = (np.mean(onsq) * i + Sq[-1])/(i+1)
        ons.append(eps)
        one.append(epe)
        oneq.append(epse)
        onsq.append(epss)