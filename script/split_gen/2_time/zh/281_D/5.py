def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i][j] = dp[i - 1][j]
            if dp[i - 1][j] and a[i - 1] % d == 0:
                dp[i][j + 1] = 1
    for i in range(n, -1, -1):
        if dp[n][i]:
            print(i)
            return
    print(-1)
main()
