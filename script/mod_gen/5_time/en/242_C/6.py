def main():
    N = int(input())
    mod = 998244353
    dp = [[0 for i in range(9*N+1)] for j in range(N+1)]
    for i in range(1,10):
        dp[1][i] = 1
    for i in range(2,N+1):
        for j in range(1,9*N+1):
            for k in range(1,10):
                if j-k>=0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= mod
    ans = 0
    for i in range(1,10):
        ans += dp[N][i]
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()