def main():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [0] * n
    for i in range(n):
        t[i], k[i] = map(int, input().split())
        a[i] = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = t[0]
    for i in range(1, n):
        dp[i] = dp[i-1] + t[i]
        for j in a[i]:
            dp[i] = min(dp[i], dp[j-1] + t[i])
    print(dp[n-1])

if __name__ == '__main__':
    main()