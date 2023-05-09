def main():
    N = int(input())
    dp = [[0,0,0] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        dp[i][0] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%1000000007
        dp[i][1] = (dp[i-1][0]+dp[i-1][2])%1000000007
        dp[i][2] = (dp[i-1][0]+dp[i-1][1])%1000000007
    print((dp[N][0]+dp[N][1]+dp[N][2])%1000000007)

if __name__ == '__main__':
    main()