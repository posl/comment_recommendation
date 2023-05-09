def main():
    h, w, k = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if j > 0:
                dp[i + 1][j - 1] += dp[i][j]
                dp[i + 1][j - 1] %= mod
            if j < w - 1:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= mod
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
    print(dp[h][k - 1])

if __name__ == '__main__':
    main()