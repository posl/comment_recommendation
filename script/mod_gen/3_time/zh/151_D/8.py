def dfs(x,y):
    global max_depth
    global depth
    global visited
    global goal_x
    global goal_y
    if x == goal_x and y == goal_y:
        max_depth = max(max_depth,depth)
        return
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<H and 0<=ny<W and visited[nx][ny] == False and maze[nx][ny] == '.':
            depth += 1
            dfs(nx,ny)
            depth -= 1
    visited[x][y] = False

if __name__ == '__main__':
    dfs()