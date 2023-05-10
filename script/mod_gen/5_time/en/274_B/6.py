def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    res = [0] * W
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                res[j] += 1
    print(*res)

if __name__ == '__main__':
    main()