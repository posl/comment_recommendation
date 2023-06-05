def solve():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for _ in range(m):
        a,b = map(int,input().split())
        c.append(a)
        y.append(b)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i][i] = x[i]
    for i in range(n):
        for j in range(i+1,n):
            dp[i][j] = dp[i][j-1] + x[j]
    dp2 = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp2[i][i] = x[i]
    for i in range(n):
        for j in range(i+1,n):
            dp2[i][j] = max(dp2[i][j-1],dp[i][j])
    ans = 0
    for i in range(1,n+1):
        for j in range(m):
            if i < c[j]:
                continue
            ans = max(ans,dp2[i-c[j]][i-1]+y[j])
    print(ans)
solve()
