def main():
    H, W = map(int, input().split())
    grid = [input() for i in range(H)]
    for j in range(W):
        cnt = 0
        for i in range(H):
            if grid[i][j] == '#':
                cnt += 1
        print(cnt, end=' ')

if __name__ == '__main__':
    main()