def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,m,a)
    a.sort(reverse=True)
    #print(a)
    dp = [-1]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(m):
            if i - a[j] >= 0:
                dp[i] = max(dp[i],dp[i-a[j]] + 1)
    #print(dp)
    ans = ""
    for i in range(dp[n]):
        for j in range(m):
            if n - a[j] >= 0 and dp[n] == dp[n-a[j]] + 1:
                ans += str(a[j])
                n -= a[j]
                break
    print(ans)
