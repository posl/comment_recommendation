def main():
    s = input()
    n = len(s)
    # dp[i][j] = 文字列 s の i 文字目までを使って、
    #            文字 c, h, o, k, u, d, a, i の j 文字目までを
    #            並べたときの場合の数
    dp = [[0] * 8 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(8):
            if s[i] == "c" and j == 0:
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == "h" and j == 1:
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == "o" and j == 2:
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == "k" and j == 3:
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == "u" and j == 4:
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == "d" and j == 5:
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == "a" and j == 6:
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == "i" and j == 7:
                dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j] += dp[i][j]
    print(dp[n][7] % (10**9 + 7))

if __name__ == '__main__':
    main()