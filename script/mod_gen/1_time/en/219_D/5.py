def main():
    N = int(input())
    X, Y = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    dp = [[[float('inf')] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                if j < X:
                    dp[i + 1][min(j + A[i], X)][k] = min(dp[i + 1][min(j + A[i], X)][k], dp[i][j][k] + 1)
                if k < Y:
                    dp[i + 1][j][min(k + B[i], Y)] = min(dp[i + 1][j][min(k + B[i], Y)], dp[i][j][k] + 1)
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
    
    ans = dp[N][X][Y]
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()