def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j > i:
                continue
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+i*a[i-1])
    print(dp[n][m])

if __name__ == '__main__':
    main()