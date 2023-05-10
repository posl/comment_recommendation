def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for _ in range(5000)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(5000):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
            dp[i+1][j+A[i]] += dp[i][j]
            dp[i+1][j+A[i]] %= mod
    ans = 0
    for i in range(5000):
        if i % 2 == 0:
            ans += dp[N][i]
            ans %= mod
    print(ans)

if __name__ == '__main__':
    main()