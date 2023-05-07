def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    MOD = 10 ** 9 + 7
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= MOD
    print((dp[N] * 2) % MOD)
    return

if __name__ == '__main__':
    main()