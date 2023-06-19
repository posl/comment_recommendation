def main():
    n,k = map(int,input().split())
    l = [0]*k
    r = [0]*k
    for i in range(k):
        l[i],r[i] = map(int,input().split())
    mod = 998244353
    dp = [0]*(n+1)
    dp[1] = 1
    dpsum = [0]*(n+1)
    dpsum[1] = 1
    for i in range(2,n+1):
        for j in range(k):
            left = i - r[j]
            right = i - l[j]
            if right < 0:
                continue
            left = max(left,1)
            dp[i] += dpsum[right] - dpsum[left-1]
        dp[i] %= mod
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= mod
    print(dp[n])

if __name__ == '__main__':
    main()