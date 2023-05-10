def main():
    n, m = map(int, input().split())
    m = m**0.5
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    dp = [[-1 for i in range(n)] for j in range(n)]
    dp[0][0] = 0
    queue = [(0,0)]
    while len(queue) > 0:
        x, y = queue.pop(0)
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and dp[nx][ny] == -1 and abs(grid[x][y] - grid[nx][ny]) <= m:
                dp[nx][ny] = dp[x][y] + 1
                queue.append((nx, ny))
    for row in dp:
        print(' '.join(map(str, row)))
