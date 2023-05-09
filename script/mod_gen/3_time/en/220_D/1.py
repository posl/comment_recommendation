def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    dp = [[0] * 10 for _ in range(n)]
    dp[0][a[0]] = 1
    for i in range(1, n):
        for j in range(10):
            dp[i][(j + a[i]) % 10] += dp[i - 1][j]
            dp[i][(j * a[i]) % 10] += dp[i - 1][j]
            dp[i][(j + a[i]) % 10] %= mod
            dp[i][(j * a[i]) % 10] %= mod
    print(*dp[-1], sep='
')

if __name__ == '__main__':
    main()