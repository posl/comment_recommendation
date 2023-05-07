def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[0] * 2 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(2):
            for k in range(10):
                ni = i + 1
                nj = j
                if k == 0:
                    nj = 1
                if k == 9:
                    nj = 1
                dp[ni][nj] += dp[i][j]
                dp[ni][nj] %= MOD
    print((dp[N][0] + dp[N][1]) % MOD)

if __name__ == '__main__':
    main()