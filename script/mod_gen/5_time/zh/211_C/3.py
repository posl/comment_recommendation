def count_s(s):
    s_len = len(s)
    chokudai = "chokudai"
    chokudai_len = len(chokudai)
    dp = [[0 for i in range(chokudai_len + 1)] for j in range(s_len + 1)]
    for i in range(s_len + 1):
        dp[i][0] = 1
    for i in range(1, s_len + 1):
        for j in range(1, chokudai_len + 1):
            if s[i - 1] == chokudai[j - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[s_len][chokudai_len] % (10 ** 9 + 7)

if __name__ == '__main__':
    count_s()