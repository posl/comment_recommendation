def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    l = 0
    r = 10**9
    while r-l > 10**-5:
        m = (l+r)/2
        t = 0
        for i in range(n):
            t += a[i]/(b[i]+m)
        if t > m:
            l = m
        else:
            r = m
    print(l)
