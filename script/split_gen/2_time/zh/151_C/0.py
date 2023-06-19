def problem151_c():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        p_,s_ = input().split()
        p.append(int(p_))
        s.append(s_)
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            ac += 1
        else:
            wa += 1
    print(ac,wa)
