def main():
    s = input()
    chokudai = "chokudai"
    mod = 10**9 + 7
    dp = [[0 for _ in range(len(chokudai)+1)] for _ in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][0] = 1
    for i in range(1,len(s)+1):
        for j in range(1,len(chokudai)+1):
            dp[i][j] = dp[i-1][j]
            if s[i-1] == chokudai[j-1]:
                dp[i][j] += dp[i-1][j-1]
                dp[i][j] %= mod
    print(dp[len(s)][len(chokudai)])

if __name__ == '__main__':
    main()