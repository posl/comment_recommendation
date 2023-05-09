def main():
    s = input()
    n = len(s)
    dp = [[float("inf")] * 2 for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + int(s[i]))
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + int(s[i]) + 1)
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + (10 - int(s[i])))
    print(dp[n][0])

if __name__ == '__main__':
    main()