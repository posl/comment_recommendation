def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    #dp[i]表示i步走到第i个格子的走法
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] = dp[i-1]*2
        if i-k>=0:
            dp[i] -= dp[i-k]
        dp[i] %= mod
    #print(dp)
    #s[i]表示前i步走到第i个格子的走法
    s = [0]*(n+1)
    for i in range(1,n+1):
        s[i] = s[i-1]+dp[i]
        s[i] %= mod
    #print(s)
    ans = [0]*k
    for i in range(1,k+1):
        ans[i-1] = (s[n]-s[n-i])%mod
    for i in ans:
        print(i)
