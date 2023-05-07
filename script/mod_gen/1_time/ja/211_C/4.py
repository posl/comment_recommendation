def main():
    S = input()
    S_len = len(S)
    ans = 0
    chokudai = 'chokudai'
    chokudai_len = len(chokudai)
    dp = [[0] * (chokudai_len + 1) for _ in range(S_len + 1)]
    for i in range(S_len + 1):
        dp[i][0] = 1
    for i in range(1, S_len + 1):
        for j in range(1, chokudai_len + 1):
            if S[i - 1] == chokudai[j - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[S_len][chokudai_len] % (10 ** 9 + 7))

if __name__ == '__main__':
    main()