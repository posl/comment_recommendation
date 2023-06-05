def solve():
    N, M, Q = map(int, input().split())
    W = [0] * (N + 1)
    V = [0] * (N + 1)
    for i in range(1, N + 1):
        W[i], V[i] = map(int, input().split())
    X = [0] * (M + 1)
    X[1:] = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        res = 0
        for i in range(1, L):
            res += V[i]
        for i in range(R + 1, M + 1):
            res += V[i]
        dp = [[0] * (N + 1) for _ in range(X[L] + 1)]
        for i in range(1, N + 1):
            for j in range(X[L], W[i] - 1, -1):
                dp[j][i] = max(dp[j][i - 1], dp[j - W[i]][i - 1] + V[i])
            for j in range(X[L] - W[i], -1, -1):
                dp[j][i] = max(dp[j][i - 1], dp[j + W[i]][i - 1] + V[i])
        res += dp[0][N]
        print(res)
