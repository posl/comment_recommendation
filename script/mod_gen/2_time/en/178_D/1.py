def main():
    S = int(input())
    MOD = 10**9 + 7
    dp = [0] * (S + 1)
    dp[0] = 1
    for i in range(3, S + 1):
        for j in range(i):
            dp[i] += dp[j]
            dp[i] %= MOD
    print(dp[S])

if __name__ == '__main__':
    main()