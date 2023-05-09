def main():
    n,m = map(int,input().split())
    grid = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i][j] = -1
    grid[0][0] = 0
    queue = [(0,0)]
    while queue:
        x,y = queue.pop(0)
        for i in range(-int(m**0.5)-1,int(m**0.5)+2):
            for j in range(-int(m**0.5)-1,int(m**0.5)+2):
                if i == 0 and j == 0:
                    continue
                if 0 <= x+i < n and 0 <= y+j < n and grid[x+i][y+j] == -1:
                    grid[x+i][y+j] = grid[x][y] + 1
                    queue.append((x+i,y+j))
    for i in range(n):
        print(*grid[i])

if __name__ == '__main__':
    main()