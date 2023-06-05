def solve():
    mod = 10**9 + 7
    S = int(input())
    dp = [[0] * (S + 1) for _ in range(S + 1)]
    dp[0][0] = 1
    for i in range(3, S + 1):
        for j in range(S + 1):
            dp[i][j] += dp[i - 1][j - i]
            if j >= i:
                dp[i][j] += dp[i][j - i]
            dp[i][j] %= mod
    print(dp[S][S])
solve()
