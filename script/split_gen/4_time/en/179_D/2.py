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
    for i in range(2,n+1):
        for j in range(k):
            if i-l[j] < 0:
                continue
            dp[i] += dp[i-l[j]]
            dp[i] %= 998244353
            if i-r[j]-1 >= 0:
                dp[i] -= dp[i-r[j]-1]
                dp[i] %= 998244353
    print(dp[n])
