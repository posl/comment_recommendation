def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * 4 for _ in range(n)]
    dp[0][0] = a[0] * p
    dp[0][1] = a[0] * q
    dp[0][2] = a[0] * r
    dp[0][3] = 0
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], a[i] * p)
        dp[i][1] = max(dp[i - 1][1], dp[i][0] + a[i] * q)
        dp[i][2] = max(dp[i - 1][2], dp[i][1] + a[i] * r)
        dp[i][3] = max(dp[i - 1][3], dp[i][2])
    print("Yes" if dp[n - 1][3] != 0 else "No")

if __name__ == '__main__':
    main()