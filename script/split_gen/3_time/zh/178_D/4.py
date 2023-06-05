def solve():
    S = int(input())
    mod = 10 ** 9 + 7
    dp = [[0 for i in range(S + 1)] for j in range(S + 1)]
    dp[0][0] = 1
    for i in range(1, S + 1):
        for j in range(3, S + 1):
            if i >= j:
                dp[i][j] = (dp[i][j - 1] + dp[i - j][j]) % mod
            else:
                dp[i][j] = dp[i][j - 1]
    print(dp[S][S])
solve()
