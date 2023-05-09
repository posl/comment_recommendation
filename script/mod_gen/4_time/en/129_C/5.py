def main():
    n,m = map(int,input().split())
    a = [0]*m
    for i in range(m):
        a[i] = int(input())
    a.append(n+1)
    a.append(0)
    a.sort()
    dp = [0]*(n+1)
    dp[0] = 1
    mod = 10**9+7
    for i in range(m+1):
        for j in range(a[i+1]-a[i]):
            dp[a[i]+j] = (dp[a[i]+j-1]+dp[a[i]+j-2])%mod
    print(dp[n])

if __name__ == '__main__':
    main()