def main():
    N, M = map(int, input().split())
    L = int(M ** 0.5)
    ans = [[-1 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                ans[i][j] = 0
            elif i == 0:
                if ans[i][j - 1] + 1 <= L:
                    ans[i][j] = ans[i][j - 1] + 1
            elif j == 0:
                if ans[i - 1][j] + 1 <= L:
                    ans[i][j] = ans[i - 1][j] + 1
            else:
                if ans[i][j - 1] + 1 <= L:
                    ans[i][j] = ans[i][j - 1] + 1
                if ans[i - 1][j] + 1 <= L:
                    if ans[i][j] == -1:
                        ans[i][j] = ans[i - 1][j] + 1
                    else:
                        ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1)
    for i in range(N):
        for j in range(N):
            if ans[i][j] != -1:
                ans[i][j] = ans[i][j] ** 2
    for i in range(N):
        print(*ans[i])

if __name__ == '__main__':
    main()