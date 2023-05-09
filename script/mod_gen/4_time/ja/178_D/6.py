def main():
    S = int(input())
    dp = [0]*(S+1)
    dp[0] = 1
    for i in range(S+1):
        for j in range(3,i+1):
            dp[i] += dp[i-j]
            dp[i] %= 10**9+7
    print(dp[S])

if __name__ == '__main__':
    main()