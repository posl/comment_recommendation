def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    i = j = 0
    while True:
        if grid[i][j] == 'U':
            if i == 0:
                print(i+1, j+1)
                return
            else:
                i -= 1
        elif grid[i][j] == 'D':
            if i == h-1:
                print(i+1, j+1)
                return
            else:
                i += 1
        elif grid[i][j] == 'L':
            if j == 0:
                print(i+1, j+1)
                return
            else:
                j -= 1
        elif grid[i][j] == 'R':
            if j == w-1:
                print(i+1, j+1)
                return
            else:
                j += 1
        else:
            print(-1)
            return

if __name__ == '__main__':
    main()