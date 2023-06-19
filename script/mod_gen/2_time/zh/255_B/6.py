def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i],y[i] = map(int,input().split())
    l = 0
    r = 10**9
    while r-l > 10**(-6):
        m = (l+r)/2
        ok = False
        for i in range(1<<k):
            lx = 10**9
            rx = -10**9
            ly = 10**9
            ry = -10**9
            for j in range(k):
                if (i>>j)&1:
                    lx = min(lx,x[a[j]-1]-m)
                    rx = max(rx,x[a[j]-1]+m)
                    ly = min(ly,y[a[j]-1]-m)
                    ry = max(ry,y[a[j]-1]+m)
            if rx-lx < ry-ly:
                continue
            ok = True
            for j in range(n):
                if lx <= x[j] and x[j] <= rx and ly <= y[j] and y[j] <= ry:
                    continue
                ng = True
                for l in range(k):
                    if (i>>l)&1:
                        if (x[j]-x[a[l]-1])**2+(y[j]-y[a[l]-1])**2 <= m**2:
                            ng = False
                if ng:
                    ok = False
                    break
            if ok:
                break
        if ok:
            r = m
        else:
            l = m
    print("{:.12f}".format(r))

if __name__ == '__main__':
    main()