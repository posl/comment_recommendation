def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [[0] * 4 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                if j == 0 and k == 2:
                    continue
                if j == 0 and k == 1:
                    continue
                if j == 1 and k == 0:
                    continue
                if j == 2 and k == 0:
                    continue
                if j == 1 and k == 2:
                    continue
                dp[i + 1][k] += dp[i][j]
                dp[i + 1][k] %= mod
    print(sum(dp[N]) % mod)

if __name__ == '__main__':
    main()