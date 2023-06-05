def main():
    N, M, K = map(int, input().split())
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                for l in range(M+1):
                    if k+j+l <= K:
                        dp[i+1][l][k+j+l] += dp[i][j][k]
    ans = 0
    for i in range(M+1):
        ans += dp[N][i][K]
    print(ans%998244353)
