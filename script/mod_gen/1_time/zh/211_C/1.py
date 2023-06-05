def main():
    s = input()
    chokudai = "chokudai"
    mod = 10**9 + 7
    dp = [[0 for _ in range(len(chokudai))] for _ in range(len(s))]
    for i in range(len(s)):
        if s[i] == chokudai[0]:
            dp[i][0] = 1
        if i > 0:
            dp[i][0] += dp[i-1][0]
            dp[i][0] %= mod
    for i in range(1, len(s)):
        for j in range(1, len(chokudai)):
            if s[i] == chokudai[j]:
                dp[i][j] = dp[i-1][j-1]
            dp[i][j] += dp[i-1][j]
            dp[i][j] %= mod
    print(dp[len(s)-1][len(chokudai)-1])

if __name__ == '__main__':
    main()