def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(list(input()))
    #print(grid)
    for i in range(H):
        count = 0
        for j in range(W):
            if grid[i][j] == "#":
                count += 1
        print(count, end=" ")
    print()

if __name__ == '__main__':
    main()