def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j + B[i] <= Y and k + A[i] <= X:
                    dp[i + 1][j + B[i]][k + A[i]] = min(dp[i + 1][j + B[i]][k + A[i]], dp[i][j][k] + 1)
    ans = dp[N][Y][X]
    if ans == float('inf'):
        ans = -1
    print(ans)
main()

if __name__ == '__main__':
    main()