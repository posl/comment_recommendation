def main():
    S = input()
    s = 'atcoder'
    n = len(S)
    m = len(s)
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif S[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min([dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1])
    print(dp[n][m])

if __name__ == '__main__':
    main()