def main():
    N = int(input())
    MOD = 998244353
    dp = [0]*10
    for i in range(1,10):
        dp[i] = 1
    
    for i in range(2,N+1):
        ndp = [0]*10
        for j in range(10):
            if j == 0:
                ndp[j] = dp[j+1]
            elif j == 9:
                ndp[j] = dp[j-1]
            else:
                ndp[j] = dp[j-1] + dp[j+1]
            ndp[j] %= MOD
        dp = ndp
    print(sum(dp)%MOD)

if __name__ == '__main__':
    main()