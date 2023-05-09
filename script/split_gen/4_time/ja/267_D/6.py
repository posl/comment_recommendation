def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.reverse()
    dp = [[0 for i in range(M+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+A[i]*(i-j))
            if i+1 < N:
                dp[i+2][j+1] = max(dp[i+2][j+1],dp[i][j]+A[i+1]*(i-j))
    print(dp[N][M])
