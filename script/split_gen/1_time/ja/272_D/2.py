def main():
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if i + j == 0:
                continue
            if i + j >= 2 * M:
                ans[i][j] = i + j
                continue
            if i + j == 1:
                continue
            if i == 0:
                ans[i][j] = ans[i][j - 1] + 1
                continue
            if j == 0:
                ans[i][j] = ans[i - 1][j] + 1
                continue
            ans[i][j] = min(ans[i - 1][j], ans[i][j - 1]) + 1
    for i in range(N):
        print(*ans[i])
