def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[-10**9 for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+1 <= m:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + (i+1)*a[i])
    print(dp[n][m])

if __name__ == '__main__':
    main()