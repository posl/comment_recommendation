def problems275_b():
    a,b,c,d,e,f = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    if a*b*c >= d*e*f:
        print((a*b*c - d*e*f)%998244353)
    else:
        print(0)
