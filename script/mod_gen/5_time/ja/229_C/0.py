def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # dp[i][j] i番目までのチーズで重さがjになるときの最大のおいしさ
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(w+1):
            if j-b[i] >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i][j-b[i]]+a[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n][w])

if __name__ == '__main__':
    main()