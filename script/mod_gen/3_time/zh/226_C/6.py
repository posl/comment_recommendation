def main():
    n = int(input())
    t = [0] * (n + 1)
    k = [0] * (n + 1)
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        t[i], k[i] = map(int, input().split())
        a[i] = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(k[i]):
            dp[a[i][j]] = max(dp[a[i][j]], dp[i] + t[i])
    print(max(dp) + t[n])

if __name__ == '__main__':
    main()