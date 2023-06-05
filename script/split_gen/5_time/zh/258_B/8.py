def main():
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input())))
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                continue
            ans = max(ans, grid[i-1][j-1]*1000 + grid[i-1][j]*100 + grid[i-1][j+1]*10 + grid[i][j+1])
            ans = max(ans, grid[i-1][j]*1000 + grid[i-1][j+1]*100 + grid[i][j+1]*10 + grid[i+1][j+1])
            ans = max(ans, grid[i-1][j+1]*1000 + grid[i][j+1]*100 + grid[i+1][j+1]*10 + grid[i+1][j])
            ans = max(ans, grid[i][j+1]*1000 + grid[i+1][j+1]*100 + grid[i+1][j]*10 + grid[i+1][j-1])
            ans = max(ans, grid[i+1][j+1]*1000 + grid[i+1][j]*100 + grid[i+1][j-1]*10 + grid[i][j-1])
            ans = max(ans, grid[i+1][j]*1000 + grid[i+1][j-1]*100 + grid[i][j-1]*10 + grid[i-1][j-1])
            ans = max(ans, grid[i+1][j-1]*1000 + grid[i][j-1]*100 + grid[i-1][j-1]*10 + grid[i-1][j])
            ans = max(ans, grid[i][j-1]*1000 + grid[i-1][j-1]*100 + grid[i-1][j]*10 + grid[i-1][j+1])
    print(ans)
