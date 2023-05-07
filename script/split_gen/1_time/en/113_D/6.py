def main():
    H, W, K = map(int, input().split())
    mod = 10**9+7
    dp = [[0]*(W+2) for _ in range(H+1)]
    dp[0][1] = 1
    for i in range(H):
        for j in range(1, W+1):
            if (dp[i][j-1] and dp[i][j+1]) or (dp[i][j-1] and j==W) or (dp[i][j+1] and j==1):
                continue
            dp[i+1][j] = dp[i][j-1] + dp[i][j+1]
    print(dp[H][K]%mod)
