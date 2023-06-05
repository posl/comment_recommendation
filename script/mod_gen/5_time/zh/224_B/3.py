def is_ok(h,w,grid):
    for i1 in range(h):
        for i2 in range(i1+1,h):
            for j1 in range(w):
                for j2 in range(j1+1,w):
                    if grid[i1][j1]+grid[i2][j2]>grid[i2][j1]+grid[i1][j2]:
                        return False
    return True
h,w=map(int,input().split())
grid=[]
for i in range(h):
    grid.append(list(map(int,input().split())))

if __name__ == '__main__':
    is_ok()