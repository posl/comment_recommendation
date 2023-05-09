def solve():
    S = input()
    N = len(S)
    dp = [[float("inf")] * 2 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        s = int(S[i])
        dp[i+1][0] = min(dp[i][0] + s, dp[i][1] + s + 1)
        dp[i+1][1] = min(dp[i][0] + (10 - s), dp[i][1] + (9 - s))
    print(min(dp[N][0], dp[N][1] + 1))
