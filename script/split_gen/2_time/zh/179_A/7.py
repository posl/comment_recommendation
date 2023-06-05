def solve():
    S = int(input())
    dp = [[0 for _ in range(S + 1)] for _ in range(S + 1)]
    dp[0][0] = 1
    for i in range(3, S + 1):
        for j in range(S + 1):
            for k in range(S - i + 1):
                if j + k <= S:
                    dp[i][j + k] += dp[i - 1][j]
                    dp[i][j + k] %= 1000000007
    print(dp[S][S])
solve()
