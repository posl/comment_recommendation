def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[0][A[0]] = 1
    for i in range(1, N):
        for j in range(10):
            dp[i][(j + A[i]) % 10] += dp[i - 1][j]
            dp[i][(j + A[i]) % 10] %= mod
            dp[i][(j * A[i]) % 10] += dp[i - 1][j]
            dp[i][(j * A[i]) % 10] %= mod
    for i in range(10):
        print(dp[N - 1][i])
