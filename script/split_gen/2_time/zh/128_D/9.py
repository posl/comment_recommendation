def problem128_d():
    n,k = map(int,input().split())
    v = list(map(int,input().split()))
    ans = 0
    for l in range(min(n,k)+1):
        for r in range(min(n,k)-l+1):
            t = v[:l]+v[n-r:]
            t.sort()
            ans = max(ans,sum(t[max(0,k-l-r):]))
    print(ans)
