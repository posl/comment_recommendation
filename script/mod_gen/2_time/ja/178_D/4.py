def main():
    s = int(input())
    dp = [0] * (s+1)
    dp[0] = 1
    for i in range(3, s+1):
        for j in range(i, s+1):
            dp[j] += dp[j-i]
    print(dp[s] % 1000000007)

if __name__ == '__main__':
    main()