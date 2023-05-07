def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = dict()
    for i in range(m):
        d[a[i]] = i + 1
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in a:
            if i - d[j] >= 0 and dp[i - d[j]] != -1:
                dp[i] = max(dp[i], dp[i - d[j]] * 10 + j)
    print(dp[n])

if __name__ == '__main__':
    main()