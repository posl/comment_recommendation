def main():
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            if i + j == 0:
                continue
            if i == 0:
                if ans[i][j - 1] != -1 and (i + j) ** 2 - (i + j - 1) ** 2 == M:
                    ans[i][j] = ans[i][j - 1] + 1
            elif j == 0:
                if ans[i - 1][j] != -1 and (i + j) ** 2 - (i + j - 1) ** 2 == M:
                    ans[i][j] = ans[i - 1][j] + 1
            else:
                if ans[i - 1][j] != -1 and (i + j) ** 2 - (i + j - 1) ** 2 == M:
                    ans[i][j] = ans[i - 1][j] + 1
                if ans[i][j - 1] != -1 and (i + j) ** 2 - (i + j - 1) ** 2 == M:
                    ans[i][j] = ans[i][j - 1] + 1
    for i in range(N):
        print(*ans[i])

if __name__ == '__main__':
    main()