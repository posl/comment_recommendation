def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # dp[i][j][k] = i 番目までの弁当を見て、たこ焼きが j 個、たい焼きが k 個あるときの、
    # 買う弁当の最小個数
    dp = [[[float('inf')] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                nj = j + A[i]
                nk = k + B[i]
                if nj <= X and nk <= Y:
                    dp[i + 1][nj][nk] = min(dp[i + 1][nj][nk], dp[i][j][k] + 1)
    ans = dp[N][X][Y]
    if ans == float('inf'):
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()