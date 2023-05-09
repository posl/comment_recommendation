def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n):
        for j in range(m + 1):
            if j == 0:
                dp[i + 1][j] = dp[i][j] + a[i]
            else:
                dp[i + 1][j] = max(dp[i][j] + a[i], dp[i][j - 1])
    print(dp[n][m])

if __name__ == '__main__':
    main()