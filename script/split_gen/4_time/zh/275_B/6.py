def problems275_b(a,b,c,d,e,f):
    if a*b*c >= d*e*f:
        return (a*b*c - d*e*f) % 998244353
    else:
        return 0
