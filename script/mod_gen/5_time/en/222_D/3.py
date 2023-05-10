def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dp = [[0] * 3001 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(a[i], b[i] + 1):
            dp[i + 1][j] = dp[i + 1][j - 1] + dp[i][j]
            dp[i + 1][j] %= 998244353
    print(dp[n][b[n - 1]])

if __name__ == '__main__':
    main()