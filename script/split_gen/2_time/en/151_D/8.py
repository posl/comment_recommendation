def main():
    H, W = map(int, input().split())
    maze = [input() for _ in range(H)]
    #print(maze)
    dist = [[-1]*W for _ in range(H)]
    #print(dist)
    que = []
    for i in range(H):
        for j in range(W):
            if maze[i][j] == ".":
                que.append((i, j))
                dist[i][j] = 0
                break
    while que:
        i, j = que.pop(0)
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            if maze[ni][nj] == "#":
                continue
            if dist[ni][nj] != -1:
                continue
            dist[ni][nj] = dist[i][j] + 1
            que.append((ni, nj))
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, dist[i][j])
    print(ans)
