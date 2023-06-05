def main():
    s = input()
    t = "atcoder"
    n = len(s)
    m = len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = j
            elif t[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1])
    print(dp[m][n])

if __name__ == '__main__':
    main()