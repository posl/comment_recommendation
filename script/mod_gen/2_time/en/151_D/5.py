def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    def bfs(sx, sy):
        dist = [[-1] * w for _ in range(h)]
        dist[sx][sy] = 0
        q = [(sx, sy)]
        while q:
            x, y = q.pop(0)
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + i, y + j
                if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '.' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        return dist
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            dist = bfs(i, j)
            for k in range(h):
                for l in range(w):
                    if s[k][l] == '#':
                        continue
                    ans = max(ans, dist[k][l])
    print(ans)

if __name__ == '__main__':
    main()