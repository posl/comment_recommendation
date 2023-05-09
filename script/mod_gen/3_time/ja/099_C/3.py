def main():
    n = int(input())
    coins = [1,6,9,36,81,216,729,1296,6561,7776,46656,59049]
    dp = [n] * (n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in coins:
            if i - j >= 0:
                dp[i] = min(dp[i],dp[i-j]+1)
    print(dp[n])

if __name__ == '__main__':
    main()