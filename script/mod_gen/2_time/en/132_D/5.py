def main():
    n,k = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(1,k+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%mod
    ans = [0 for _ in range(k+1)]
    for i in range(1,k+1):
        ans[i] = (dp[n-k+1][i] * dp[k-1][i-1])%mod
    for i in range(1,k+1):
        print(ans[i])

if __name__ == '__main__':
    main()