def main():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(input())
    visited = [[0 for i in range(w)] for j in range(h)]
    curx, cury = 0, 0
    while True:
        if visited[curx][cury] == 1:
            print(-1)
            break
        visited[curx][cury] = 1
        if grid[curx][cury] == 'U':
            if curx == 0:
                print(curx + 1, cury + 1)
                break
            else:
                curx -= 1
        elif grid[curx][cury] == 'D':
            if curx == h - 1:
                print(curx + 1, cury + 1)
                break
            else:
                curx += 1
        elif grid[curx][cury] == 'L':
            if cury == 0:
                print(curx + 1, cury + 1)
                break
            else:
                cury -= 1
        elif grid[curx][cury] == 'R':
            if cury == w - 1:
                print(curx + 1, cury + 1)
                break
            else:
                cury += 1
        else:
            print(curx + 1, cury + 1)
            break

if __name__ == '__main__':
    main()