def main():
    N = int(input())
    MOD = 998244353
    # dp[i][j][k] := i 桁目まで決めて、差が j であるものの個数
    dp = [[[0] * 2 for _ in range(10)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(10):
            for k in range(2):
                for d in range(1, 10):
                    ni, nj, nk = i + 1, j + d, k
                    if d == 1:
                        nk = 1
                    if nj >= 10:
                        continue
                    dp[ni][nj][nk] += dp[i][j][k]
                    dp[ni][nj][nk] %= MOD
    print(sum(dp[N][1:]) % MOD)

if __name__ == '__main__':
    main()