def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0] * (B[-1] + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(B[i] + 1):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
            if j < A[i]:
                dp[i + 1][A[i]] += dp[i][j]
                dp[i + 1][A[i]] %= MOD
            else:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
    print(dp[N][-1])
