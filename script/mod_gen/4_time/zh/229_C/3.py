def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(w+1):
            if j >= b[i]:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-b[i]]+a[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n][w])

if __name__ == '__main__':
    main()