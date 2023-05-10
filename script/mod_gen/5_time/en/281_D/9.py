def solve():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    # dp[i][j][k] = 1 if we can make the sum j with k terms from the first i elements of A
    dp = [[[0 for _ in range(K + 1)] for _ in range(D)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(1, N + 1):
        for j in range(D):
            for k in range(K + 1):
                if dp[i - 1][j][k]:
                    dp[i][j][k] = 1
                    if k < K:
                        dp[i][j][k + 1] = 1
                    if j + A[i - 1] < D:
                        dp[i][j + A[i - 1]][k] = 1
                        if k < K:
                            dp[i][j + A[i - 1]][k + 1] = 1
    ans = -1
    for i in range(D - 1, -1, -1):
        if dp[N][i][K]:
            ans = i
            break
    print(ans * D)
solve()

if __name__ == '__main__':
    solve()