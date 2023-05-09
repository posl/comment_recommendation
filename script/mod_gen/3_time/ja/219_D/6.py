def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    dp = [[[0 for k in range(Y + 1)] for j in range(X + 1)] for i in range(N + 1)]
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
                if j - A[i] >= 0 and k - B[i] >= 0:
                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j - A[i]][k - B[i]] + 1)
    if dp[N][X][Y] == 0:
        print(-1)
    else:
        print(dp[N][X][Y])

if __name__ == '__main__':
    main()