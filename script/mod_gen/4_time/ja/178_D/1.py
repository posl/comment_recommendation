def main():
    S = int(input())
    mod = 10**9 + 7
    dp = [0] * (S+1)
    dp[0] = 1
    for i in range(3, S+1):
        dp[i] = (dp[i-1] + dp[i-3]) % mod
    print(dp[S])

if __name__ == '__main__':
    main()