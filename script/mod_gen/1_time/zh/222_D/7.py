def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(a[i - 1], b[i - 1] + 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod
    print(dp[n][b[n - 1]])

if __name__ == '__main__':
    main()