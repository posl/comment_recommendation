def main():
    s = int(input())
    dp = [0 for _ in range(s+1)]
    dp[0] = 1
    
    for i in range(3, s+1):
        for j in range(i, s+1):
            dp[j] = (dp[j] + dp[j-i]) % (10**9 + 7)
    
    print(dp[s])
main()

if __name__ == '__main__':
    main()