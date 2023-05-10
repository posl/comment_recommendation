def main():
    N, M = map(int, input().split())
    grid = [[-1 for i in range(N)] for j in range(N)]
    grid[0][0] = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == -1:
                continue
            for k in range(N):
                for l in range(N):
                    if grid[k][l] == -1:
                        if (i-k)**2 + (j-l)**2 == M:
                            grid[k][l] = grid[i][j] + 1
    for i in range(N):
        print(' '.join(map(str, grid[i])))

if __name__ == '__main__':
    main()