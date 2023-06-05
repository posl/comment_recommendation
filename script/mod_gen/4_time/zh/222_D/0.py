def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    mod = 998244353
    dp = [[0 for i in range(3001)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(a[i], b[i]+1):
            dp[i+1][j] = dp[i][j]
        for j in range(1, 3001):
            dp[i+1][j] += dp[i+1][j-1]
            dp[i+1][j] %= mod
    print(dp[n][3000])

if __name__ == '__main__':
    main()