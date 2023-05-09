def main():
    N,M,Q = map(int,input().split())
    W = [0 for i in range(N)]
    V = [0 for i in range(N)]
    X = [0 for i in range(M)]
    for i in range(N):
        W[i],V[i] = map(int,input().split())
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L,R = map(int,input().split())
        #print(L,R)
        X_ = X[:L-1] + X[R:]
        #print(X_)
        dp = [[0 for i in range(sum(X_)+1)] for j in range(N+1)]
        for i in range(N):
            for j in range(sum(X_)+1):
                if j < W[i]:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = max(dp[i][j],dp[i][j-W[i]]+V[i])
        print(dp[N][sum(X_)])
