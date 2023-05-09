def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    
    # dp[i][j] = (i個の整数の和がjとなるような選び方の数)
    dp = [[0] * (N*10**9+1) for _ in range(N+1)]
    dp[0][0] = 1
    
    for i in range(N):
        for j in range(N*10**9+1):
            dp[i+1][j] = dp[i][j]
            if j - A[i] >= 0:
                dp[i+1][j] += dp[i][j-A[i]]
            dp[i+1][j] %= MOD
    
    ans = 0
    for i in range(1, N+1):
        for j in range(N*10**9+1):
            if dp[i][j] > 0 and j % i == 0:
                ans += 1
                ans %= MOD
    
    print(ans)

if __name__ == '__main__':
    main()