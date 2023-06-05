def main():
    N,M,K = map(int,input().split())
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1,M+1):
        dp[1][i][i] = 1
    for i in range(2,N+1):
        for j in range(1,M+1):
            for k in range(1,K+1):
                if k-j>=0:
                    dp[i][j][k] = dp[i][j][k-j] + dp[i-1][j-1][k-j]
    print(dp[N][M][K] % 998244353)
