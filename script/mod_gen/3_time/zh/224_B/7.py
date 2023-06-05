def solve(h,w,grid):
    for i in range(h):
        for j in range(w):
            for k in range(i+1,h):
                for l in range(j+1,w):
                    if grid[i][j]+grid[k][l]>grid[i][l]+grid[k][j]:
                        return False
    return True

if __name__ == '__main__':
    solve()