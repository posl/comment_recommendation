def solve():
    H, W, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    # dp[i][j]: the number of the amidakuji with i horizontal lines and j vertical lines
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j > 0:
                dp[i + 1][j] += dp[i][j - 1]
                dp[i + 1][j] %= MOD
            if j < W - 1:
                dp[i + 1][j] += dp[i][j + 1]
                dp[i + 1][j] %= MOD
            if j == 0 or j == W - 1:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD
    print(dp[H][K - 1])

if __name__ == '__main__':
    solve()