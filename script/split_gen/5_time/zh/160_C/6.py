def solve(k,n,a):
    a = sorted(a)
    m = k-a[-1]+a[0]
    for i in range(1,n):
        m = max(m,a[i]-a[i-1])
    return k-m
k,n = map(int,input().split())
a = list(map(int,input().split()))
print(solve(k,n,a))
