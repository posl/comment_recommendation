def main():
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    dp = [[-float('inf') for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            if j > 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + a[i]*(j-1))
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    print(dp[n][m])

if __name__ == '__main__':
    main()