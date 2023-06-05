def solve():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        X_ = X[:L - 1] + X[R:]
        N_ = len(X_)
        dp = [[0] * (sum(X_) + 1) for _ in range(N_ + 1)]
        for i in range(N_):
            for j in range(sum(X_) + 1):
                if j < X_[i]:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = max(dp[i][j], dp[i][j - X_[i]] + V[i])
        print(dp[-1][-1])
solve()
