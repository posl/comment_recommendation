def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(10):
            dp = [[0] * 10 for _ in range(N)]
            dp[0][(i + j) % 10] = 1
            dp[0][(i * j) % 10] += 1
            for k in range(N - 1):
                for l in range(10):
                    dp[k + 1][(l + A[k + 1]) % 10] += dp[k][l]
                    dp[k + 1][(l + A[k + 1]) % 10] %= MOD
                    dp[k + 1][(l * A[k + 1]) % 10] += dp[k][l]
                    dp[k + 1][(l * A[k + 1]) % 10] %= MOD
            ans[i] += dp[N - 1][j]
            ans[i] %= MOD
    for i in range(10):
        print(ans[i])
