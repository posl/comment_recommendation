def main():
    H, W = list(map(int, input().split()))
    grid = [list(input()) for _ in range(H)]
    i, j = 0, 0
    for _ in range(H * W):
        if grid[i][j] == 'U':
            if i == 0:
                print(-1)
                exit()
            i -= 1
        elif grid[i][j] == 'D':
            if i == H - 1:
                print(-1)
                exit()
            i += 1
        elif grid[i][j] == 'L':
            if j == 0:
                print(-1)
                exit()
            j -= 1
        elif grid[i][j] == 'R':
            if j == W - 1:
                print(-1)
                exit()
            j += 1
        else:
            print('error')
            exit()
    print(i + 1, j + 1)

if __name__ == '__main__':
    main()