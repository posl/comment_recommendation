def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # MOD = 10
    dp = [[0] * 10 for _ in range(N)]
    dp[0][A[0]] = 1
    for i in range(1, N):
        for j in range(10):
            dp[i][(j + A[i]) % 10] += dp[i - 1][j]
            dp[i][(j * A[i]) % 10] += dp[i - 1][j]
            dp[i][(j + A[i]) % 10] %= MOD
            dp[i][(j * A[i]) % 10] %= MOD
    print(*dp[N - 1], sep='
')

if __name__ == '__main__':
    main()