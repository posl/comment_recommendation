def solve():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        #print(L, R)
        #print(W)
        #print(V)
        #print(X)
        #print()
        X_ = X[:L-1] + X[R:]
        #print(X_)
        dp = [0] * (sum(X_) + 1)
        for i in range(N):
            for j in range(sum(X_), W[i]-1, -1):
                dp[j] = max(dp[j], dp[j-W[i]] + V[i])
        print(dp[-1])
solve()
