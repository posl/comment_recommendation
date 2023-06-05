def main():
    s = input()
    t = 'atcoder'
    n = len(s)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = i
            elif i == 0:
                dp[i][j] = j
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    print(dp[n][m])

if __name__ == '__main__':
    main()