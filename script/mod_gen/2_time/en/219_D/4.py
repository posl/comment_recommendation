def main():
    n = int(input())
    x, y = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    dp = [[-1] * (x + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(x + 1):
            if dp[i][j] == -1:
                continue
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + a[i] <= x:
                dp[i + 1][j + a[i]] = max(dp[i + 1][j + a[i]], dp[i][j] + b[i])
    ans = -1
    for i in range(x + 1):
        if dp[n][i] >= y:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()