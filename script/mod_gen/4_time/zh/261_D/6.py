def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for _ in range(m):
        ci, yi = map(int, input().split())
        c.append(ci)
        y.append(yi)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i + 1][0] = dp[i][0] + x[i]
    for i in range(n):
        for j in range(1, n + 1):
            if j <= i + 1:
                dp[i + 1][j] = max(dp[i][j - 1] + y[j - 1], dp[i][j] + x[i])
            else:
                dp[i + 1][j] = dp[i][j] + x[i]
    ans = 0
    for i in range(n + 1):
        ans = max(ans, dp[n][i])
    print(ans)

if __name__ == '__main__':
    main()