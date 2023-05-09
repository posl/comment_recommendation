def main():
    N = int(input())
    X,Y = map(int,input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    dp = [[[0 for i in range(Y+1)] for j in range(X+1)] for k in range(N+1)]
    for k in range(N):
        for i in range(X+1):
            for j in range(Y+1):
                if i-A[k]>=0 and j-B[k]>=0:
                    dp[k+1][i][j] = max(dp[k][i-A[k]][j-B[k]]+1,dp[k][i][j])
                dp[k+1][i][j] = max(dp[k+1][i-A[k]][j],dp[k+1][i][j-B[k]],dp[k+1][i][j])
    if dp[N][X][Y] == 0:
        print(-1)
    else:
        print(dp[N][X][Y])

if __name__ == '__main__':
    main()