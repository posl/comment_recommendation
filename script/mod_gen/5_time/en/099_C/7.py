def main():
    N = int(input())
    #print(N)
    dp = [0] * (N+1)
    dp[1] = 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1
        j = 6
        while j <= i:
            dp[i] = min(dp[i], dp[i-j] + 1)
            j *= 6
        j = 9
        while j <= i:
            dp[i] = min(dp[i], dp[i-j] + 1)
            j *= 9
    print(dp[N])

if __name__ == '__main__':
    main()