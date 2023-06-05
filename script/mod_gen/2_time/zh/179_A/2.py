def main():
    S = int(input())
    mod = 10**9+7
    dp = [[0 for _ in range(S+1)] for _ in range(S+1)]
    dp[0][0] = 1
    for i in range(1,S+1):
        for j in range(1,S+1):
            if i <= j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-i]
            else:
                dp[i][j] = dp[i-1][j-1]
    print(dp[S][S]%mod)

if __name__ == '__main__':
    main()