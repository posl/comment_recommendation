def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'U':
                if i == 0:
                    print(-1)
                    return
                else:
                    i -= 1
            elif grid[i][j] == 'D':
                if i == H - 1:
                    print(-1)
                    return
                else:
                    i += 1
            elif grid[i][j] == 'L':
                if j == 0:
                    print(-1)
                    return
                else:
                    j -= 1
            elif grid[i][j] == 'R':
                if j == W - 1:
                    print(-1)
                    return
                else:
                    j += 1
            if grid[i][j] == 'G':
                print(i+1, j+1)
                return

if __name__ == '__main__':
    main()