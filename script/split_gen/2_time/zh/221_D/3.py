def problems221_d():
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    c = [0]*(10**9+1)
    for i in range(n):
        c[a[i]] += 1
        c[a[i]+b[i]] -= 1
    for i in range(1, 10**9+1):
        c[i] += c[i-1]
    d = [0]*(n+1)
    for i in range(1, 10**9+1):
        if c[i] > 0:
            d[c[i]] += 1
    for i in range(1, n+1):
        print(d[i], end=' ')
