def problems265_b():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(m):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    time = 0
    for i in range(n-1):
        time += a[i]
        if time >= t:
            print('No')
            return
        if i+1 in x:
            time = min(time + y[x.index(i+1)], t)
    print('Yes')
    return
