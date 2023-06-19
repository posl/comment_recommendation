def main():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(list(input()))
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'U' and i != 0:
                i -= 1
            elif grid[i][j] == 'D' and i != h - 1:
                i += 1
            elif grid[i][j] == 'L' and j != 0:
                j -= 1
            elif grid[i][j] == 'R' and j != w - 1:
                j += 1
    print(i + 1, j + 1)

if __name__ == '__main__':
    main()