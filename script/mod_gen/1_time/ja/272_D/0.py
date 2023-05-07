def main():
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] != -1:
                if i != N - 1:
                    if ans[i + 1][j] == -1:
                        ans[i + 1][j] = ans[i][j] + 1
                    else:
                        ans[i + 1][j] = min(ans[i + 1][j], ans[i][j] + 1)
                if j != N - 1:
                    if ans[i][j + 1] == -1:
                        ans[i][j + 1] = ans[i][j] + 1
                    else:
                        ans[i][j + 1] = min(ans[i][j + 1], ans[i][j] + 1)
    for i in range(N):
        for j in range(N):
            if ans[i][j] != -1:
                if i != 0:
                    if ans[i - 1][j] == -1:
                        ans[i - 1][j] = ans[i][j] + 1
                    else:
                        ans[i - 1][j] = min(ans[i - 1][j], ans[i][j] + 1)
                if j != 0:
                    if ans[i][j - 1] == -1:
                        ans[i][j - 1] = ans[i][j] + 1
                    else:
                        ans[i][j - 1] = min(ans[i][j - 1], ans[i][j] + 1)
    for i in range(N):
        for j in range(N):
            if ans[i][j] != -1:
                if i != N - 1:
                    if ans[i + 1][j] == -1:
                        ans[i + 1][j] = ans[i][j] + 1
                    else:
                        ans[i + 1][j] = min(ans[i + 1][j], ans[i][j] + 1)
                if j != N - 1:
                    if ans[i][j + 1] == -1:

if __name__ == '__main__':
    main()