def problems275_b(a,b,c,d,e,f):
    if a*b*c >= d*e*f:
        return (a*b*c - d*e*f) % 998244353
    else:
        return 0

if __name__ == '__main__':
    problems275_b()