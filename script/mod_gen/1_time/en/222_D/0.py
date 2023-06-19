def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(i + 1):
            dp[i + 1][j] += dp[i][j] * max(0, min(B[i], A[j] + j) - A[j] + 1)
            dp[i + 1][j + 1] += dp[i][j] * max(0, min(B[i], A[j] + j + 1) - A[j] - j)
            dp[i + 1][j] %= MOD
            dp[i + 1][j + 1] %= MOD
    print(sum(dp[N]) % MOD)
main()
