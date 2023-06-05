def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    xy = [list(map(int,input().split())) for _ in range(m)]
    a.append(0)
    a.append(0)
    a.sort()
    xy.sort()
    dp = [0]*(n+1)
    for x,y in xy:
        dp[x] = y
    for i in range(1,n+1):
        dp[i] = max(dp[i],dp[i-1]+a[i-1])
    if dp[n] >= t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()