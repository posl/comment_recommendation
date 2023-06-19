def solve():
    n,k = map(int,input().split())
    v = list(map(int,input().split()))
    ans = 0
    for i in range(min(n,k)+1):
        for j in range(min(n,k)-i+1):
            a = v[:i]
            b = v[n-j:]
            c = a + b
            c.sort()
            ans = max(ans,sum(c[max(0,k-i-j):]))
    print(ans)
solve()
