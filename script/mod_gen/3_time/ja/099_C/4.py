def main():
    N = int(input())
    dp = [10**9]*(N+1)
    dp[0] = 0
    for i in range(1,N+1):
        for j in range(1,i+1):
            if i < 6**j:
                break
            dp[i] = min(dp[i],dp[i-6**j]+1)
        for j in range(1,i+1):
            if i < 9**j:
                break
            dp[i] = min(dp[i],dp[i-9**j]+1)
    print(dp[N])

if __name__ == '__main__':
    main()