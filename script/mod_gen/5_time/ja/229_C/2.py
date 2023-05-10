def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # dp[i][j] i番目までのチーズで重さがjの時の最大のおいしさ
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_i] + v_i)
    # dp[0][j] = 0
    # dp[i][0] = 0
    dp = [[0 for j in range(w+1)] for i in range(n+1)]
    for i in range(n):
        for j in range(w+1):
            if j < b[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-b[i]] + a[i])
    print(dp[n][w])

if __name__ == '__main__':
    main()