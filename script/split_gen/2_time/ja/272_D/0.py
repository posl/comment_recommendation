def main():
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            if (i ** 2 + j ** 2) == M:
                ans[i][j] = 1
    for i in range(N):
        for j in range(N):
            if ans[i][j] == 1:
                continue
            if ans[i][j] == -1:
                ans[i][j] = 2
            for k in range(N):
                for l in range(N):
                    if ans[k][l] == -1:
                        continue
                    if (i - k) ** 2 + (j - l) ** 2 == M:
                        if ans[i][j] == -1:
                            ans[i][j] = ans[k][l] + 1
                        else:
                            ans[i][j] = min(ans[i][j], ans[k][l] + 1)
    for i in range(N):
        for j in range(N):
            print(ans[i][j], end = " ")
        print()
