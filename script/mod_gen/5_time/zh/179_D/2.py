def main():
    n,k = map(int,input().split())
    left = []
    right = []
    for i in range(k):
        a,b = map(int,input().split())
        left.append(a)
        right.append(b)
    mod = 998244353
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(1,n):
        dp[i+1] = (dp[i+1]+dp[i])%mod
        for j in range(k):
            if i+left[j] <= n:
                dp[i+left[j]] = (dp[i+left[j]]+dp[i])%mod
            if i+right[j]+1 <= n:
                dp[i+right[j]+1] = (dp[i+right[j]+1]-dp[i]+mod)%mod
    print(dp[n])

if __name__ == '__main__':
    main()