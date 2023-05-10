def main():
    N, M = map(int, input().split())
    M2 = M ** 0.5
    M2 = int(M2)
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            if i - M2 >= 0 and ans[i - M2][j] == -1:
                ans[i - M2][j] = ans[i][j] + 1
            if i + M2 < N and ans[i + M2][j] == -1:
                ans[i + M2][j] = ans[i][j] + 1
            if j - M2 >= 0 and ans[i][j - M2] == -1:
                ans[i][j - M2] = ans[i][j] + 1
            if j + M2 < N and ans[i][j + M2] == -1:
                ans[i][j + M2] = ans[i][j] + 1
    for i in range(N):
        print(*ans[i])

if __name__ == '__main__':
    main()