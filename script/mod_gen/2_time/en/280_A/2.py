def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    count = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                count += 1
    print(count)

if __name__ == '__main__':
    main()