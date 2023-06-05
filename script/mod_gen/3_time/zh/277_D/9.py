def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n):
        if a[i] >= m:
            a[i] = a[i]%m
    res = 0
    for i in range(n):
        if a[i] != 0:
            res += a[i]
            if i != n-1:
                a[i+1] -= m-a[i]
    print(res)
solve()
