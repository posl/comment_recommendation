def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[0] * 4 for _ in range(N)]
    dp[0] = [1] * 4
    for i in range(1, N):
        for j in range(4):
            for k in range(4):
                if j == 0 and k == 2 or j == 0 and k == 3 or j == 1 and k == 2 or j == 2 and k == 0:
                    continue
                dp[i][j] += dp[i - 1][k]
    print(sum(dp[N - 1]) % MOD)

if __name__ == '__main__':
    main()