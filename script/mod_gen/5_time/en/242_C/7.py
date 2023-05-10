def solve():
    N = int(input())
    dp = [[0]*10 for _ in range(N+1)]
    dp[0][0] = 1
    mod = 998244353
    for i in range(N):
        for j in range(10):
            for k in range(10):
                if abs(k-j) <= 1:
                    dp[i+1][k] += dp[i][j]
                    dp[i+1][k] %= mod
    print(sum(dp[N])%mod)

if __name__ == '__main__':
    solve()