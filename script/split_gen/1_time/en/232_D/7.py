def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[0][0] = True
    queue = [[0, 0]]
    count = 0
    while queue:
        x, y = queue.pop(0)
        count += 1
        for dx, dy in [[1, 0], [0, 1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])
    print(count)
