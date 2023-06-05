def solve():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for q in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        dp = [[0] * (M + 1) for _ in range(M + 1)]
        for i in range(N):
            w = W[i]
            v = V[i]
            for j in range(M, 0, -1):
                for k in range(j - 1, -1, -1):
                    if X[j - 1] >= w:
                        dp[j][k] = max(dp[j][k], dp[j - 1][k] + v)
                    if k > 0:
                        dp[j][k] = max(dp[j][k], dp[j][k - 1] + v)
        print(dp[M][R - L])
solve()
