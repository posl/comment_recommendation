def main():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(input())
    #print(grid)
    i = 0
    j = 0
    for _ in range(H*W):
        if grid[i][j] == "U":
            if i == 0:
                print(i+1, j+1)
                break
            else:
                i = i-1
        elif grid[i][j] == "D":
            if i == H-1:
                print(i+1, j+1)
                break
            else:
                i = i+1
        elif grid[i][j] == "L":
            if j == 0:
                print(i+1, j+1)
                break
            else:
                j = j-1
        elif grid[i][j] == "R":
            if j == W-1:
                print(i+1, j+1)
                break
            else:
                j = j+1
        else:
            print(-1)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()