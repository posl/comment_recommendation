def main():
    s = input()
    n = len(s)
    mod = 10**9 + 7
    # dp[i][j] = (i文字目まで見て、j文字目まで見つけたときのパターン数)
    dp = [[0] * 8 for i in range(n)]
    if s[0] == 'c':
        dp[0][0] = 1
    for i in range(n-1):
        for j in range(8):
            if s[i+1] == 'c' and j == 0:
                dp[i+1][j] = dp[i][j] + 1
            elif s[i+1] == 'h' and j == 1:
                dp[i+1][j] = dp[i][j] + dp[i][j-1]
            elif s[i+1] == 'o' and j == 2:
                dp[i+1][j] = dp[i][j] + dp[i][j-1]
            elif s[i+1] == 'k' and j == 3:
                dp[i+1][j] = dp[i][j] + dp[i][j-1]
            elif s[i+1] == 'u' and j == 4:
                dp[i+1][j] = dp[i][j] + dp[i][j-1]
            elif s[i+1] == 'd' and j == 5:
                dp[i+1][j] = dp[i][j] + dp[i][j-1]
            elif s[i+1] == 'a' and j == 6:
                dp[i+1][j] = dp[i][j] + dp[i][j-1]
            elif s[i+1] == 'i' and j == 7:
                dp[i+1][j] = dp[i][j] + dp[i][j-1]
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n-1][7] % mod)

if __name__ == '__main__':
    main()