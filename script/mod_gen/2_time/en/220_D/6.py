def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j]: i桁目まで見て、最終的にjになる場合の数
    dp = [[0 for _ in range(10)] for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(10):
            dp[i + 1][(j + A[i]) % 10] += dp[i][j]
            dp[i + 1][(j + A[i]) % 10] %= MOD
            dp[i + 1][(j * A[i]) % 10] += dp[i][j]
            dp[i + 1][(j * A[i]) % 10] %= MOD
    for i in range(10):
        print(dp[N][i])

if __name__ == '__main__':
    main()