def main():
    H,W = map(int,input().split())
    grid = [list(input()) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    i = j = 0
    while True:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if grid[i][j] == 'U':
            if i == 0:
                print(i+1,j+1)
                return
            else:
                i -= 1
        elif grid[i][j] == 'D':
            if i == H-1:
                print(i+1,j+1)
                return
            else:
                i += 1
        elif grid[i][j] == 'L':
            if j == 0:
                print(i+1,j+1)
                return
            else:
                j -= 1
        elif grid[i][j] == 'R':
            if j == W-1:
                print(i+1,j+1)
                return
            else:
                j += 1
