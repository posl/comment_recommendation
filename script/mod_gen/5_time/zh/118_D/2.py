def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    dp = [0]*(n+1)
    for i in range(1,n+1):
        dp[i] = float("-inf")
        for j in range(m):
            if i-a[j]>=0:
                dp[i] = max(dp[i],dp[i-a[j]]*10+a[j])
    print(dp[n])

if __name__ == '__main__':
    main()