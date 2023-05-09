def solve(S, T):
    N = len(S)
    M = len(T)
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return N - dp[N][M]
S = input()
T = input()
print(solve(S, T))
