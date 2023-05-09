def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(n+1):
        if dp[i] == -1:
            continue
        for j in range(m):
            if i+a[j] <= n:
                dp[i+a[j]] = max(dp[i+a[j]],dp[i]*10+j+1)
    print(dp[n])

if __name__ == '__main__':
    main()