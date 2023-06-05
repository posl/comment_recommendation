def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    C = []
    Y = []
    for i in range(M):
        c,y = map(int,input().split())
        C.append(c)
        Y.append(y)
    #print(N,M,X,C,Y)
    #print(X[0:3])
    #print(C[0:3])
    #print(Y[0:3])
    #print(X[0:3])
    #print(C[0:3])
    #print(Y[0:3])
    #print(X[0:3])
    #print(C[0:3])
    #print(Y[0:3])
    #print(X[0:3])
    #print(C[0:3])
    #print(Y[0:3])
    #print(X[0:3])
    #print(C[0:3])
    #print(Y[0:3])
    #print(X[0:3])
    #print(C[0:3])
    #print(Y[0:3])
    #print(X[0:3])
    #print(C[0:3])
    #print(Y[0:3])
    #print(X[0:3])
    #print(C[0:3])
    #print(Y[0:3])
    dp = [[0 for i in range(N+1)] for j in range(N+1)]
    for i in range(N):
        dp[i+1][1] = dp[i][1] + X[i]
    for i in range(N):
        for j in range(2,N+1):
            dp[i+1][j] = max(dp[i][j-1] + X[i],dp[i][j])
    #print(dp)
    ans = 0
    for i in range(N):
        for j in range(N+1):
            if dp[i][j] != 0:
                if j in C:
                    ans = max(ans,dp[i][j]+Y[C.index(j)])
                else:
                    ans = max(ans,dp[i][j])
    print(ans)

if __name__ == '__main__':
    main()