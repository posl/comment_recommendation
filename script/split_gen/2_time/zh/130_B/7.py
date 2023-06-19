def problems130_b():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i]+l[i])
    count = 0
    for i in d:
        if i <= x:
            count += 1
    print(count)
