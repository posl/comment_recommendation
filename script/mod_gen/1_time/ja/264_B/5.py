def main():
    R, C = map(int, input().split())
    grid = []
    for i in range(15):
        grid.append([])
        for j in range(15):
            if (i + j) % 2 == 0:
                grid[i].append("black")
            else:
                grid[i].append("white")
    print(grid[R - 1][C - 1])

if __name__ == '__main__':
    main()