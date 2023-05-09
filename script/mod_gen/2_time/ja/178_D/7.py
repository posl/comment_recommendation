def main():
    S = int(input())
    dp = [0 for i in range(S+1)]
    dp[0] = 1
    for i in range(3,S+1):
        for j in range(S-i+1):
            dp[i+j] += dp[j]
            dp[i+j] %= 10**9+7
    print(dp[S])

if __name__ == '__main__':
    main()