def main():
    N,M = map(int,input().split())
    a = [0]*M
    for i in range(M):
        a[i] = int(input())
    # dp[i] = iにたどり着くまでの方法
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,N+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1]+dp[i-2])%1000000007
    print(dp[N])

if __name__ == '__main__':
    main()