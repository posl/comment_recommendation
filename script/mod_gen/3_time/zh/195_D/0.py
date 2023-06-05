def solve():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    Query = []
    for i in range(Q):
        l, r = map(int, input().split())
        Query.append([l, r])
    for q in Query:
        l, r = q[0], q[1]
        X_ = X[:l-1] + X[r:]
        W_ = W[:l-1] + W[r:]
        V_ = V[:l-1] + V[r:]
        dp = [[0 for i in range(max(X_) + 1)] for j in range(len(W_) + 1)]
        for i in range(len(W_)):
            for j in range(len(dp[0])):
                if j >= W_[i]:
                    dp[i + 1][j] = max(dp[i][j], dp[i][j - W_[i]] + V_[i])
                else:
                    dp[i + 1][j] = dp[i][j]
        print(dp[-1][-1])

if __name__ == '__main__':
    solve()