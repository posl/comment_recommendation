def main():
    input = sys.stdin.readline
    N, X = map(int, input().split())
    L = [None] * N
    A = [None] * N
    for i in range(N):
        L[i], *A[i] = map(int, input().split())
    #dp[i][j]: the number of ways to pick i balls so that the product of the numbers written on the picked balls is j
    dp = [[0] * (X + 1) for _ in range(N + 1)]
    dp[0][1] = 1
    for i in range(N):
        for j in range(X + 1):
            for k in range(L[i]):
                if j * A[i][k] <= X:
                    dp[i + 1][j * A[i][k]] += dp[i][j]
    print(dp[N][X])

if __name__ == '__main__':
    main()