def main():
    N, M = map(int, input().split())
    ans = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            ans[i][j] = (i + j) * (i + j) + (i - j) * (i - j)
    for i in range(N):
        for j in range(N):
            if ans[i][j] == M:
                ans[i][j] = 1
            elif ans[i][j] < M:
                ans[i][j] = 2
            else:
                ans[i][j] = -1
    for i in range(N):
        print(*ans[i])
