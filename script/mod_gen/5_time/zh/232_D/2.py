def dfs(x,y):
    global ans
    if x == H-1 and y == W-1:
        ans += 1
        return
    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != '#':
                dfs(nx,ny)
        return
H,W = map(int,input().split())
maze = [input() for i in range(H)]
ans = 0
dx = [0,1]
dy = [1,0]
dfs(0,0)
print(ans)

if __name__ == '__main__':
    dfs()