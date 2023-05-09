def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0] * (X + 1) for _ in range(Y + 1)]
    for i in range(N):
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if j >= A[i] and k >= B[i]:
                    dp[k][j] = max(dp[k][j], dp[k - B[i]][j - A[i]] + 1)
    if dp[Y][X] == 0:
        print(-1)
    else:
        print(N - dp[Y][X])

if __name__ == '__main__':
    main()