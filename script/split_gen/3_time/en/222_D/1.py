def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N + 1):
            for k in range(A[i], B[i] + 1):
                if j == 0:
                    dp[i + 1][j] += dp[i][j] * (B[i] - A[i] + 1)
                elif k >= A[j - 1]:
                    dp[i + 1][j] += dp[i][j - 1]
                dp[i + 1][j] %= MOD
    print(sum(dp[N]) % MOD)
