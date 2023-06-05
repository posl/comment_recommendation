def main():
    s = input()
    chokudai = 'chokudai'
    mod = 10 ** 9 + 7
    n = len(s)
    m = len(chokudai)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(n + 1):
        dp[0][i] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if chokudai[i - 1] == s[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i][j - 1]) % mod
            else:
                dp[i][j] = dp[i][j - 1]
    print(dp[-1][-1])

if __name__ == '__main__':
    main()