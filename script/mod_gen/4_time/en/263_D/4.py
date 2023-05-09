def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[float('inf')] * 3 for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(3):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + a[i]*l)
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + a[i]*r)
    print(dp[n][2])

if __name__ == '__main__':
    main()