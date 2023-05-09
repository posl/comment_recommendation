def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            dp[i + 1][j] += dp[i][j] * max(0, B[i] - j)
            dp[i + 1][j + 1] += dp[i][j] * max(0, j + 1 - A[i])
            dp[i + 1][j] %= MOD
            dp[i + 1][j + 1] %= MOD
    ans = 0
    for j in range(N + 1):
        ans += dp[N][j]
    print(ans % MOD)

if __name__ == '__main__':
    main()