def solve():
    N, M, Q = map(int, input().split())
    W = [0] * (N + 1)
    V = [0] * (N + 1)
    for i in range(1, N + 1):
        W[i], V[i] = map(int, input().split())
    X = [0] * (M + 1)
    for i in range(1, M + 1):
        X[i] = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        X_ = [0] * (M + 1)
        for i in range(1, M + 1):
            if i < L or R < i:
                X_[i] = X[i]
        dp = [0] * (sum(X_) + 1)
        for i in range(1, N + 1):
            for j in range(sum(X_), W[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - W[i]] + V[i])
        print(max(dp))

if __name__ == '__main__':
    solve()