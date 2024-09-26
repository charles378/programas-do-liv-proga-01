def calcu(h, a, p):
    sbruto = h * a
    sliquido = sbruto - (sbruto*p)/100
    return sbruto, sliquido