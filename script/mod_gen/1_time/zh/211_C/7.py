def main():
    s = input()
    s_len = len(s)
    chokudai = 'chokudai'
    chokudai_len = len(chokudai)
    dp = [[0] * (s_len + 1) for _ in range(chokudai_len + 1)]
    for i in range(s_len + 1):
        dp[0][i] = 1
    for i in range(1, chokudai_len + 1):
        for j in range(1, s_len + 1):
            if chokudai[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    print(dp[-1][-1] % (10 ** 9 + 7))

if __name__ == '__main__':
    main()