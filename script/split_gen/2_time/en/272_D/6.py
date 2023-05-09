def solve(N, M):
    if M == 1:
        return [[0] * N for _ in range(N)]
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(1, N):
        ans[0][i] = ans[0][i-1] + 1
        ans[i][0] = ans[i-1][0] + 1
    for i in range(1, N):
        for j in range(1, N):
            x = i + j
            y = i - j
            if M == x * x:
                ans[i][j] = ans[i-1][j] + 1
            if M == y * y:
                ans[i][j] = ans[i][j-1] + 1
            if ans[i][j-1] != -1 and ans[i-1][j] != -1:
                ans[i][j] = min(ans[i][j-1] + 1, ans[i-1][j] + 1)
    return ans
