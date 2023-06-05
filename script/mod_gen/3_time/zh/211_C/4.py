def main():
    s = input()
    s_len = len(s)
    mod = 10**9 + 7
    chokudai = 'chokudai'
    dp = [[0 for _ in range(8)] for _ in range(s_len)]
    for i in range(s_len):
        if s[i] == chokudai[0]:
            dp[i][0] = 1
    for i in range(1, s_len):
        for j in range(8):
            if s[i] == chokudai[j]:
                if j == 0:
                    dp[i][j] = (dp[i][j] + 1) % mod
                else:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % mod
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % mod
    print(dp[s_len-1][7])

if __name__ == '__main__':
    main()