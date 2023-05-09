def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    grid = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            grid[(i + j) % 3][c[i][j] - 1] += 1
    ans = 10 ** 9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and i != k and j != k:
                    tmp = 0
                    for l in range(C):
                        tmp += D[l][i] * grid[0][l]
                        tmp += D[l][j] * grid[1][l]
                        tmp += D[l][k] * grid[2][l]
                    ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()