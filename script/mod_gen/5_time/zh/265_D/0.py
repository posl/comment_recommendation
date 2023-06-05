def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * 4 for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = max(dp[i-1][0], p*a[i-1])
        dp[i][1] = max(dp[i-1][1], dp[i][0] + q*a[i-1])
        dp[i][2] = max(dp[i-1][2], dp[i][1] + r*a[i-1])
    print(dp[n][2])

if __name__ == '__main__':
    main()