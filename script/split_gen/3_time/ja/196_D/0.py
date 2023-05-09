def main():
    h, w, a, b = map(int, input().split())
    dp = [[0] * (1 << w) for _ in range(h + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(1 << w):
            dp[i + 1][j] += dp[i][j >> 1]
            if j & 1 == 0 and j & 2 == 0 and (j & 1 << (w - 1)) == 0:
                dp[i][j | 3] += dp[i][j]
            if j & 1 == 0 and (j & 1 << (w - 1)) == 0 and a > 0:
                dp[i][j | 1 | 1 << (w - 1)] += dp[i][j]
            if j & 1 == 0 and b > 0:
                dp[i][j | 1] += dp[i][j]
            if j & 1 << (w - 1) == 0 and b > 0:
                dp[i][j | 1 << (w - 1)] += dp[i][j]
    print(dp[h][0])
