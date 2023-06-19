def get_max_step(h,w,grid):
    max_step = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                max_step = max(max_step, bfs(i,j,h,w,grid))
    return max_step

if __name__ == '__main__':
    get_max_step()