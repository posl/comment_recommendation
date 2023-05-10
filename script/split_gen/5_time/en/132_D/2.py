def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    dp[0][0] = 1
    for i in range(1, K+1):
        for j in range(N+1):
            if j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%mod
    ans = 0
    for i in range(1, K+1):
        ans = (ans + dp[i][N-K]*dp[K-i][K-1])%mod
    print(ans)
