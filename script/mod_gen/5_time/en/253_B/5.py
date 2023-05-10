def main():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(list(input()))
    # print(grid)
    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'o':
                count += 1
    if count == 1:
        print(1)
    elif count == 2:
        print(0)
    else:
        print(3)

if __name__ == '__main__':
    main()