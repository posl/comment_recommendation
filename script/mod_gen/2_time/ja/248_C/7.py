def main():
    N, M, K = map(int, input().split())
    # dp[i][j] := i 個の整数からなる数列で、その総和が j となるような数列の個数
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K + 1):
            for k in range(M + 1):
                if j + k > K:
                    break
                dp[i + 1][j + k] += dp[i][j]
                dp[i + 1][j + k] %= 998244353
    print(dp[N][K])

if __name__ == '__main__':
    main()