def solve(S):
    N = len(S)
    mod = 10**9 + 7
    dp = [[0] * 9 for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1
    for i in range(1,N+1):
        for j in range(1,9):
            if S[i-1] == 'chokudai'[j-1]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][8] % mod
