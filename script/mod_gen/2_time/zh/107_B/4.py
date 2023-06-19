def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    row = [0] * H
    col = [0] * W
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                row[i] = 1
                col[j] = 1
    for i in range(H):
        if row[i] == 1:
            for j in range(W):
                if col[j] == 1:
                    print(grid[i][j], end = '')
            print()

if __name__ == '__main__':
    main()