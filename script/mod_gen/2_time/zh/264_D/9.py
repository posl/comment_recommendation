def main():
    s = input()
    atcoder = 'atcoder'
    s_len = len(s)
    atcoder_len = len(atcoder)
    dp = [[0] * (s_len + 1) for _ in range(atcoder_len + 1)]
    for i in range(1, atcoder_len + 1):
        dp[i][0] = 1
    for i in range(1, atcoder_len + 1):
        for j in range(1, s_len + 1):
            if atcoder[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    print(dp[atcoder_len][s_len] % (10 ** 9 + 7))

if __name__ == '__main__':
    main()