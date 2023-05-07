def solve():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c0,y0 = map(int,input().split())
        c.append(c0)
        y.append(y0)
    dp = [0]*(n+1)
    dp[0] = x[0]
    for i in range(1,n):
        dp[i] = dp[i-1]+x[i]
        for j in range(m):
            if i+1>=c[j]:
                dp[i] = max(dp[i],dp[i-c[j]]+x[i]+y[j]*(c[j]-1))
    print(max(dp))
    return

if __name__ == '__main__':
    solve()