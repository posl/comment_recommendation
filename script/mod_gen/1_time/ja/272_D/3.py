def main():
    N, M = map(int, input().split())
    ans = [[-1 for _ in range(N)] for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            for k in range(4):
                ni = i + [1, 0, -1, 0][k]
                nj = j + [0, 1, 0, -1][k]
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                if ans[ni][nj] != -1:
                    continue
                if (i - ni) ** 2 + (j - nj) ** 2 == M:
                    ans[ni][nj] = ans[i][j] + 1
    for i in range(N):
        print(*ans[i])
main()

if __name__ == '__main__':
    main()