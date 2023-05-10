def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.insert(0, 0)
    dp = [[float('inf') for _ in range(2)] for _ in range(n+2)]
    dp[0][0] = 0
    dp[0][1] = 0
    for i in range(1, n+2):
        dp[i][0] = min(dp[i-1][0]+a[i], dp[i-1][1]+max(a[i]-1, 0)+l)
        dp[i][1] = min(dp[i-1][0]+max(-a[i]+1, 0)+r, dp[i-1][1]+max(abs(a[i-1]-a[i])+max(-a[i]+1, 0)+r, abs(a[i-1]-a[i])+max(a[i]-1, 0)+l))
    print(dp[n+1][0])
main()

if __name__ == '__main__':
    main()