def problems100_d():
    n,m = map(int,input().split())
    x,y,z = [],[],[]
    for i in range(n):
        a,b,c = map(int,input().split())
        x.append(a)
        y.append(b)
        z.append(c)
    ans = 0
    for i in range(2**3):
        for j in range(2**3):
            for k in range(2**3):
                if i+j+k == m:
                    a,b,c = 0,0,0
                    for l in range(n):
                        a += x[l]*(-1 if (i>>0)&1 else 1)
                        b += y[l]*(-1 if (j>>0)&1 else 1)
                        c += z[l]*(-1 if (k>>0)&1 else 1)
                    ans = max(ans,abs(a)+abs(b)+abs(c))
    print(ans)
problems100_d()
