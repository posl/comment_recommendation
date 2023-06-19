def main():
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input())))
    # print(grid)
    ans = 0
    for i in range(n):
        for j in range(n):
            ans = max(ans, grid[i][j])
    print(ans)

if __name__ == '__main__':
    main()