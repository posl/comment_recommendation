def main():
    #input
    N = int(input())
    
    #calculate
    #1 yen
    dp = [0] * (N+1)
    #6 yen, 6^2(=36) yen, 6^3(=216) yen, ...
    #9 yen, 9^2(=81) yen, 9^3(=729) yen, ...
    for i in range(1, N+1):
        dp[i] = dp[i-1] + 1
        j = 6
        while i >= j:
            dp[i] = min(dp[i], dp[i-j] + 1)
            j *= 6
        j = 9
        while i >= j:
            dp[i] = min(dp[i], dp[i-j] + 1)
            j *= 9
    
    #output
    print(dp[N])

if __name__ == '__main__':
    main()