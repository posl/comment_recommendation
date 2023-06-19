def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(10):
            dp = [[0] * 10 for _ in range(N + 1)]
            dp[0][i] = 1
            for k in range(N):
                dp[k + 1][(dp[k][j] + A[k]) % 10] += dp[k][j]
                dp[k + 1][(dp[k][j] * A[k]) % 10] += dp[k][j]
                dp[k + 1][(dp[k][j] + A[k]) % 10] %= mod
                dp[k + 1][(dp[k][j] * A[k]) % 10] %= mod
            ans[j] += dp[N][j]
            ans[j] %= mod
    for i in ans:
        print(i)
