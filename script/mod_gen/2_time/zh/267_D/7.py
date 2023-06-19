def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    dp = [[0 for i in range(M+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = max(dp[i][j+1],dp[i][j]+A[i]*(j+1))
    print(dp[N][M])

if __name__ == '__main__':
    main()