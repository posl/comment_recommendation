def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j] は i 個目までの要素で、合計が j のものの個数
    dp = [[0] * (sum(A) + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(sum(A) + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = dp[i][j] + dp[i][j - A[i]] * 2
            else:
                dp[i + 1][j] = dp[i][j]
            dp[i + 1][j] %= MOD
    ans = 0
    for i in range(1, N + 1):
        ans += dp[i][sum(A) // 2] * pow(2, N - i, MOD)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()