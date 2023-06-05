def problems185_b():
    n, m, t = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    now = n
    for i in range(m):
        now -= (a[i] - b[i-1])
        if now <= 0:
            print('No')
            return
        now += (b[i] - a[i])
        if now > n:
            now = n
    now -= (t - b[m-1])
    if now <= 0:
        print('No')
        return
    print('Yes')
