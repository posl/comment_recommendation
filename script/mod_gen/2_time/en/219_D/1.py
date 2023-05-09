def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[10**9] * 301 for i in range(301)] for j in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X+1):
            for k in range(Y+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                dp[i+1][min(j+A[i], X)][min(k+B[i], Y)] = min(dp[i+1][min(j+A[i], X)][min(k+B[i], Y)], dp[i][j][k]+1)
    if dp[N][X][Y] == 10**9:
        print(-1)
    else:
        print(dp[N][X][Y])

if __name__ == '__main__':
    main()