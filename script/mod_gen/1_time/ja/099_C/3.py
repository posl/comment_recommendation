def main():
    N=int(input())
    dp=[0 for i in range(N+1)]
    for i in range(N+1):
        dp[i]=i
        for j in range(1,i):
            if 6**j>i:
                break
            dp[i]=min(dp[i],dp[i-6**j]+1)
        for j in range(1,i):
            if 9**j>i:
                break
            dp[i]=min(dp[i],dp[i-9**j]+1)
    print(dp[N])

if __name__ == '__main__':
    main()