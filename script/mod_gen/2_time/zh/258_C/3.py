def main():
    N = int(input())
    grid = []
    for i in range(N):
        grid.append(list(map(int, input())))
    ans = 0
    for i in range(N):
        for j in range(N):
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue
                    tmp = grid[i][j]
                    ni, nj = i, j
                    for k in range(N - 1):
                        ni += di
                        nj += dj
                        if ni == -1:
                            ni = N - 1
                        elif ni == N:
                            ni = 0
                        if nj == -1:
                            nj = N - 1
                        elif nj == N:
                            nj = 0
                        tmp *= 10
                        tmp += grid[ni][nj]
                    ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()