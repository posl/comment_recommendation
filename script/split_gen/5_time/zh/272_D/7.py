def main():
    N,M = map(int,input().split())
    grid = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                grid[i][j] = 0
            else:
                grid[i][j] = float("inf")
    for i in range(M):
        a,b = map(int,input().split())
        grid[a-1][b-1] = 1
        grid[b-1][a-1] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                grid[i][j] = min(grid[i][j],grid[i][k]+grid[k][j])
    for i in range(N):
        for j in range(N):
            if grid[i][j] == float("inf"):
                grid[i][j] = -1
    for i in range(N):
        print(*grid[i])
