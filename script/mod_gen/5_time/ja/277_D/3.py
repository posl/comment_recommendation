def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.append(a[0]+m)
    dp = [0]*(n+1)
    for i in range(n):
        dp[i+1] = dp[i]+min(a[i+1]-a[i],m-a[i+1]+a[i])
    ans = 10**18
    for i in range(n+1):
        now = dp[i]
        now += (m-a[i])*(n-i)
        ans = min(ans,now)
    print(ans)

if __name__ == '__main__':
    main()