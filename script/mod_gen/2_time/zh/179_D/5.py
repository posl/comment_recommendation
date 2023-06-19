def main():
    n,k = map(int,input().split())
    l = [0]*k
    r = [0]*k
    for i in range(k):
        l[i],r[i] = map(int,input().split())
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2,n+1):
        for j in range(k):
            dp[i] += dp[max(0,i-r[j]-1)]-dp[max(0,i-l[j]-2)]
            dp[i] %= 998244353
    print(dp[n])
main()
