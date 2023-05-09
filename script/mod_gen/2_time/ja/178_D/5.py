def main():
    mod = 10**9 + 7
    S = int(input())
    dp = [0] * (S + 1)
    dp[0] = 1
    for i in range(1, S + 1):
        for j in range(3, S + 1):
            if i - j >= 0:
                dp[i] += dp[i - j]
                dp[i] %= mod
    print(dp[S])

if __name__ == '__main__':
    main()