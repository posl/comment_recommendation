def main():
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            for k in range(1, int(M ** 0.5) + 1):
                if i + k < N:
                    if ans[i + k][j] == -1:
                        ans[i + k][j] = ans[i][j] + 1
                    else:
                        ans[i + k][j] = min(ans[i + k][j], ans[i][j] + 1)
                if j + k < N:
                    if ans[i][j + k] == -1:
                        ans[i][j + k] = ans[i][j] + 1
                    else:
                        ans[i][j + k] = min(ans[i][j + k], ans[i][j] + 1)
                if i - k >= 0:
                    if ans[i - k][j] == -1:
                        ans[i - k][j] = ans[i][j] + 1
                    else:
                        ans[i - k][j] = min(ans[i - k][j], ans[i][j] + 1)
                if j - k >= 0:
                    if ans[i][j - k] == -1:
                        ans[i][j - k] = ans[i][j] + 1
                    else:
                        ans[i][j - k] = min(ans[i][j - k], ans[i][j] + 1)
    for i in range(N):
        print(*ans[i])
