def f(N, W, A):
    A.sort()
    dp = [[0 for i in range(W + 1)] for j in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(W + 1):
            if j - A[i - 1] >= 0:
                if dp[i - 1][j - A[i - 1]] == 1:
                    dp[i][j] = 1
                elif dp[i - 1][j - A[i - 1]] == 2:
                    dp[i][j] = 2
            if dp[i - 1][j] == 1:
                dp[i][j] = 1
            elif dp[i - 1][j] == 2:
                dp[i][j] = 2
            if dp[i][j] == 0:
                dp[i][j] = 3
    ans = 0
    for i in range(W + 1):
        if dp[N][i] == 1:
            ans += 1
    return ans

if __name__ == '__main__':
    f()