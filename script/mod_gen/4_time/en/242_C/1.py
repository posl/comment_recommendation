def main():
    N = int(input())
    dp = [[0 for i in range(10)] for j in range(N)]
    for i in range(1,10):
        dp[0][i] = 1
    for i in range(1,N):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    ans = 0
    for i in range(10):
        ans += dp[N-1][i]
    print(ans % 998244353)

if __name__ == '__main__':
    main()