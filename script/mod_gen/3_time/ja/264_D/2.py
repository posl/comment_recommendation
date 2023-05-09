def main():
    s = input()
    t = "atcoder"
    dp = [[float("inf")] * (len(s) + 1) for _ in range(len(t) + 1)]
    for i in range(len(t) + 1):
        dp[i][0] = 0
    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            if t[i - 1] == s[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
    print(dp[-1][-1])

if __name__ == '__main__':
    main()