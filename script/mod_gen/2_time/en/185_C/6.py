def main():
    L = int(input())
    dp = [0]*(L+1)
    dp[0] = 1
    for i in range(1,L+1):
        for j in range(1,i):
            dp[i] += dp[i-j]*(i-j+1)
    print(dp[-1])

if __name__ == '__main__':
    main()