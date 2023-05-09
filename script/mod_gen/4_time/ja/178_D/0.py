def main():
    s = int(input())
    mod = 10**9 + 7
    dp = [0] * (s+1)
    dp[0] = 1
    for i in range(3, s+1):
        for j in range(s-i+1):
            dp[i+j] += dp[j]
            dp[i+j] %= mod
    print(dp[s])

if __name__ == '__main__':
    main()