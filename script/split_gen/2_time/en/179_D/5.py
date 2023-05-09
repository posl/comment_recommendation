def main():
    n,k = map(int,input().split())
    l = []
    r = []
    for i in range(k):
        a,b = map(int,input().split())
        l.append(a)
        r.append(b)
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = dp[1] + 1
    s = [0]*(n+1)
    s[1] = 1
    s[2] = 2
    for i in range(3,n+1):
        for j in range(k):
            dp[i] += s[i-l[j]] - s[i-r[j]-1]
        dp[i] %= 998244353
        s[i] = s[i-1] + dp[i]
    print(dp[n])
