def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[0 for k in range(Y + 1)] for j in range(X + 1)] for i in range(N + 1)]
    for i in range(N + 1):
        dp[i][0][0] = 1
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                if dp[i][j][k] == 1:
                    dp[i + 1][j][k] = 1
                    if j + A[i] <= X and k + B[i] <= Y:
                        dp[i + 1][j + A[i]][k + B[i]] = 1
    ans = 100000
    for i in range(N + 1):
        if dp[i][X][Y] == 1:
            ans = min(ans, i)
    if ans == 100000:
        print(-1)
    else:
        print(ans)
main()
