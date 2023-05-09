def main():
    H, W, K = map(int, input().split())
    dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
    dp[0][1] = 1
    mod = 10**9+7
    for i in range(1, H+1):
        for j in range(1, W+1):
            dp[i][j] = dp[i-1][j-1] * dp[i-1][j] * 2 + dp[i-1][j]**2
            dp[i][j] %= mod
    print(dp[H][K])
