def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    C = [0]*M
    Y = [0]*M
    for i in range(M):
        C[i],Y[i] = map(int,input().split())
    #print(N,M)
    #print(X)
    #print(C)
    #print(Y)
    #print()
    dp = [[0]*(N+1) for _ in range(M+1)]
    for i in range(1,N+1):
        dp[0][i] = X[i-1]
    for i in range(1,M+1):
        for j in range(1,N+1):
            dp[i][j] = max(dp[i][j],dp[i][j-1])
            if j >= C[i-1]:
                dp[i][j] = max(dp[i][j],dp[i-1][j-C[i-1]]+Y[i-1])
    print(dp[M][N])
