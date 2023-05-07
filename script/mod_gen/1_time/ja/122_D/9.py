def main():
    MOD = 10**9 + 7
    N = int(input())
    dp = [[0] * 4 for _ in range(N + 1)]
    dp[0] = [1] * 4
    for i in range(N):
        for j in range(4):
            for k in range(4):
                if j == 0 and k == 2 or j == 0 and k == 3 or j == 1 and k == 2:
                    continue
                if j == 2 and k == 0 or j == 3 and k == 0 or j == 2 and k == 1:
                    continue
                dp[i + 1][k] += dp[i][j]
                dp[i + 1][k] %= MOD
    print(sum(dp[N]) % MOD)

if __name__ == '__main__':
    main()