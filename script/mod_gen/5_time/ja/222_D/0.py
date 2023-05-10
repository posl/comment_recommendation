def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for i in range(3001)] for j in range(3001)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(a[i], b[i]+1):
            dp[i+1][j] = dp[i+1][j-1] + dp[i][j]
            dp[i+1][j] %= mod
        for j in range(b[i]+1, 3001):
            dp[i+1][j] = dp[i+1][j-1]
    print(dp[n][3000])

if __name__ == '__main__':
    main()