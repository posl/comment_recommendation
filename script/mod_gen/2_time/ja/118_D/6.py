def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    match = [2,5,5,4,5,6,3,7,6]
    a.sort(reverse=True)
    dp = [0]*(n+1)
    for i in range(1,n+1):
        for j in range(m):
            if i-match[a[j]-1] >= 0:
                dp[i] = max(dp[i-match[a[j]-1]]*10+a[j],dp[i])
    print(dp[n])

if __name__ == '__main__':
    main()