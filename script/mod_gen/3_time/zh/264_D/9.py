def main():
    s = input()
    atcoder = 'atcoder'
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(8)]
    if s[0] == 'a':
        dp[0][0] = 1
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + 1 if s[i] == 'a' else dp[0][i - 1]
    for i in range(1, 8):
        for j in range(1, n):
            if s[j] == atcoder[i]:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    print(dp[7][n - 1] % (10 ** 9 + 7))

if __name__ == '__main__':
    main()