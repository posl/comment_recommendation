def solve():
    S = int(input())
    MOD = 10**9 + 7
    # dp[i][j] := 表示使用前i个数，和为j的序列的个数
    dp = [[0] * (S+1) for _ in range(S+1)]
    dp[0][0] = 1
    for i in range(1, S+1):
        for j in range(S+1):
            dp[i][j] = dp[i-1][j]
            if j - i >= 0:
                dp[i][j] += dp[i][j-i]
            dp[i][j] %= MOD
    print(dp[S][S])
solve()
