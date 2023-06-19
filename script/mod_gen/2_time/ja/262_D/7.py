def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    #dp[i][j] := i番目までの数でj個選んだ時の平均値の合計
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            dp[i+1][j] += dp[i][j]*(j+1)
            dp[i+1][j] %= mod
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod
    ans = 0
    for i in range(n):
        ans += dp[n][i]*a[i]
        ans %= mod
    print(ans)
solve()
