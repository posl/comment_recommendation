def main():
    n,l,r = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] = a[i] - l
    # print(a)
    # print(sum(a))
    dp = [[0 for i in range(2)] for j in range(n+1)]
    for i in range(n):
        dp[i+1][0] = max(dp[i][0], dp[i][1])
        dp[i+1][1] = max(dp[i][0] + a[i], dp[i][1] + a[i])
    print(max(dp[n][0], dp[n][1]) + n * r)
    return

if __name__ == '__main__':
    main()