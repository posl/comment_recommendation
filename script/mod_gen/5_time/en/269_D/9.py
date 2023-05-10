def dfs(i,j):
    global grid
    stack = [(i,j)]
    while stack:
        i,j = stack.pop()
        if grid[i][j] == 0:
            grid[i][j] = 1
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < 2002 and 0 <= nj < 2002:
                    if grid[ni][nj] == 0:
                        stack.append((ni,nj))
    return 1
N = int(input())
grid = [[0 for j in range(2002)] for i in range(2002)]
for _ in range(N):
    X,Y = map(int,input().split())
    grid[X+1000][Y+1000] = 2
ans = 0
for i in range(2002):
    for j in range(2002):
        if grid[i][j] == 2:
            ans += dfs(i,j)
print(ans)

if __name__ == '__main__':
    dfs()