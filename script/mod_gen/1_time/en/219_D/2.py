def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[0] * 301 for i in range(301)] for i in range(N + 1)]
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
                if j + A[i] <= X and k + B[i] <= Y:
                    dp[i + 1][j + A[i]][k + B[i]] = max(dp[i + 1][j + A[i]][k + B[i]], dp[i][j][k] + 1)
    if dp[N][X][Y] == 0:
        print(-1)
    else:
        print(dp[N][X][Y])

if __name__ == '__main__':
    main()