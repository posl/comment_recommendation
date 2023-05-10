def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    # dp[i][j]: i個のボールをj個のグループに分ける場合の数
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        dp[i][1] = 1
        for j in range(2, K+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-j][j]) % mod
    print(dp[N][K])
