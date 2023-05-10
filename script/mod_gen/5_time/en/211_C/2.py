def main():
    s = input()
    chokudai = "chokudai"
    mod = 10**9 + 7
    dp = [[0 for _ in range(len(chokudai) + 1)] for _ in range(len(s) + 1)]
    dp[0][0] = 1
    for i in range(len(s)):
        for j in range(len(chokudai) + 1):
            if j == 0:
                dp[i + 1][j] = dp[i][j]
            else:
                if s[i] == chokudai[j - 1]:
                    dp[i + 1][j] = dp[i][j] + dp[i][j - 1]
                else:
                    dp[i + 1][j] = dp[i][j]
            dp[i + 1][j] %= mod
    print(dp[len(s)][len(chokudai)])

if __name__ == '__main__':
    main()