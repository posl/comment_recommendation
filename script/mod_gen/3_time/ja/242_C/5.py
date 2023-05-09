def main():
    n = int(input())
    dp = [[0 for _ in range(13)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(10):
            for k in range(13):
                dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
                dp[i + 1][(k * 10 + j) % 13] %= 998244353
    print(dp[n][5])
main()

if __name__ == '__main__':
    main()