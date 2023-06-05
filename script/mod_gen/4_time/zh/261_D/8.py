def solve():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    C = []
    Y = []
    for i in range(M):
        c,y = map(int,input().split())
        C.append(c)
        Y.append(y)
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,i+1):
            dp[i][j] = max(dp[i][j],dp[i-1][j-1]+X[i-1])
            for k in range(M):
                if j == C[k]:
                    dp[i][j] = max(dp[i][j],dp[i-C[k]][j-C[k]]+Y[k])
    print(max(dp[N]))

if __name__ == '__main__':
    solve()