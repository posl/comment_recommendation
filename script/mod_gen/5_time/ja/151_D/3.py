def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    # 4方向
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            # BFS
            dist = [[-1] * w for _ in range(h)]
            dist[i][j] = 0
            q = [(i, j)]
            while q:
                y, x = q.pop(0)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or w <= nx or ny < 0 or h <= ny:
                        continue
                    if s[ny][nx] == '#':
                        continue
                    if dist[ny][nx] != -1:
                        continue
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
            for k in range(h):
                for l in range(w):
                    if dist[k][l] == -1:
                        continue
                    ans = max(ans, dist[k][l])
    print(ans)

if __name__ == '__main__':
    main()