def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[False for i in range(Y+1)] for j in range(X+1)] for k in range(N+1)]
    dp[0][0][0] = True
    for i in range(N):
        for j in range(X+1):
            for k in range(Y+1):
                if not dp[i][j][k]:
                    continue
                dp[i+1][j][k] = True
                if j + A[i] <= X and k + B[i] <= Y:
                    dp[i+1][j+A[i]][k+B[i]] = True
    for i in range(X, X+1):
        for j in range(Y, Y+1):
            if dp[N][i][j]:
                print(i + j)
                return
    print(-1)
