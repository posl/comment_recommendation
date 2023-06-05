def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i+1][0] = dp[i][0] + a[i]
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i][j] = dp[i-1][j-1] + a[i-1] * j
    ans = 0
    for i in range(m+1):
        ans = max(ans,dp[n][i])
    print(ans)
solve()
