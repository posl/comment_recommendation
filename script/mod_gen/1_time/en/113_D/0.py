def main():
    h, w, k = map(int, input().split())
    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if j == 0:
                dp[i + 1][j] = dp[i][j + 1] + dp[i][j]
            elif j == w - 1:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j] + dp[i][j + 1]
    print(dp[h][k - 1] % (10 ** 9 + 7))

if __name__ == '__main__':
    main()