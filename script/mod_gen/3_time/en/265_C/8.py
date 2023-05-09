def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    #print(grid)
    #print(H, W)
    x, y = 0, 0
    #print(x, y)
    count = 0
    while True:
        if count > H * W:
            print(-1)
            break
        if grid[x][y] == "U":
            if x == 0:
                print(x+1, y+1)
                break
            else:
                x -= 1
        elif grid[x][y] == "D":
            if x == H-1:
                print(x+1, y+1)
                break
            else:
                x += 1
        elif grid[x][y] == "L":
            if y == 0:
                print(x+1, y+1)
                break
            else:
                y -= 1
        elif grid[x][y] == "R":
            if y == W-1:
                print(x+1, y+1)
                break
            else:
                y += 1
        count += 1
main()

if __name__ == '__main__':
    main()