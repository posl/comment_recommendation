def solve(N, M, A):
    # dp[i] := ちょうどi本のマッチを使って作れる最大の整数
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for a in A:
            if i - a >= 0 and dp[i - a] != -1:
                dp[i] = max(dp[i], dp[i - a] * 10 + a)
    return dp[N]
