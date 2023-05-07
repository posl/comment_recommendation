def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [[0] * 2 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        dp[i+1][0] = (dp[i][0] * 8 + dp[i][1] * 9) % mod
        dp[i+1][1] = (dp[i][0] + dp[i][1] * 10) % mod
    print((dp[N][0] + dp[N][1]) % mod)

if __name__ == '__main__':
    main()