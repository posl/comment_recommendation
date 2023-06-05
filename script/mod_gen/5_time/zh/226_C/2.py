def main():
    n = int(input())
    t = [0]*(n+1)
    k = [0]*(n+1)
    a = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        t[i],k[i] = map(int,input().split())
        a[i] = list(map(int,input().split()))
    dp = [0]*(n+1)
    for i in range(1,n+1):
        for j in range(k[i]):
            dp[i] = max(dp[i],dp[a[i][j]]+t[a[i][j]])
        dp[i] = max(dp[i],dp[i-1]+t[i])
    print(dp[n])

if __name__ == '__main__':
    main()