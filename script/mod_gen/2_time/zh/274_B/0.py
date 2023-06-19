def main():
    H, W = map(int, input().split())
    #print(H,W)
    grid = [input() for _ in range(H)]
    #print(grid)
    for i in range(H):
        print(grid[i].count('#'))

if __name__ == '__main__':
    main()