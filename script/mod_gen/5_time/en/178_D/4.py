def main():
    S = int(input())
    dp = [0] * (S+1)
    dp[0] = 1
    for i in range(3, S+1):
        for j in range(0, i-2):
            dp[i] += dp[j]
            dp[i] %= 1000000007
    print(dp[S])

if __name__ == '__main__':
    main()