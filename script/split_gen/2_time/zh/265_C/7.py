def main():
    h,w = map(int,input().split())
    grid = [list(input()) for i in range(h)]
    pos = [0,0]
    visited = [[0]*w for i in range(h)]
    while True:
        visited[pos[0]][pos[1]] = 1
        if grid[pos[0]][pos[1]] == 'U':
            if pos[0] == 0:
                print(-1)
                break
            elif visited[pos[0]-1][pos[1]] == 1:
                print(-1)
                break
            else:
                pos[0] -= 1
        elif grid[pos[0]][pos[1]] == 'D':
            if pos[0] == h-1:
                print(-1)
                break
            elif visited[pos[0]+1][pos[1]] == 1:
                print(-1)
                break
            else:
                pos[0] += 1
        elif grid[pos[0]][pos[1]] == 'L':
            if pos[1] == 0:
                print(-1)
                break
            elif visited[pos[0]][pos[1]-1] == 1:
                print(-1)
                break
            else:
                pos[1] -= 1
        elif grid[pos[0]][pos[1]] == 'R':
            if pos[1] == w-1:
                print(-1)
                break
            elif visited[pos[0]][pos[1]+1] == 1:
                print(-1)
                break
            else:
                pos[1] += 1
        if visited[pos[0]][pos[1]] == 1:
            print(pos[0]+1,pos[1]+1)
            break
    return 0
