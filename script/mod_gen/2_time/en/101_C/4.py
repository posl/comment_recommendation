def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0]*(n+1)
    for i in range(n):
        dp[i+1] = dp[i] + a[i]
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, dp[i+k]-dp[i])
    print(ans)

if __name__ == '__main__':
    main()