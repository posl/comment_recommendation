def solve():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a1,p1,x1 = map(int,input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    for i in range(n):
        for j in range(i+1,n):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
                p[i],p[j] = p[j],p[i]
                x[i],x[j] = x[j],x[i]
    for i in range(n):
        if x[i] > 0:
            print(p[i])
            return
    print(-1)
    return
