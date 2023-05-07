def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c_, y_ = map(int, input().split())
        c.append(c_)
        y.append(y_)
    dp = [0] * (n+1)
    for i in range(n):
        dp[i+1] = max(dp[i+1], dp[i] + x[i])
        for j in range(m):
            if i + c[j] <= n:
                dp[i+c[j]] = max(dp[i+c[j]], dp[i] + y[j])
    print(dp[n])

if __name__ == '__main__':
    main()