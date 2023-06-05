def problems151_c():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        a,b = input().split()
        p.append(int(a))
        s.append(b)
    ac = 0
    wa = 0
    for i in range(n):
        if s[i] == 'AC':
            ac += 1
            wa += p[i]
    print(ac,wa)
problems151_c()
