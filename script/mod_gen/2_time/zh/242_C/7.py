def main():
    N = int(input())
    #dp[i][j] : i桁目まで決めたとき、i桁目の数字がjのときの数
    dp = [[0 for _ in range(10)] for _ in range(N+1)]
    for j in range(1,10):
        dp[1][j] = 1
    for i in range(2,N+1):
        for j in range(0,10):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
    ans = 0
    for j in range(0,10):
        ans += dp[N][j]
    print(ans % 998244353)

if __name__ == '__main__':
    main()