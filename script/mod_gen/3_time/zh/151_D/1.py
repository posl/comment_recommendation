def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                t = [[-1] * w for _ in range(h)]
                t[i][j] = 0
                q = [(i, j)]
                for x, y in q:
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '.' and t[nx][ny] < 0:
                            t[nx][ny] = t[x][y] + 1
                            q.append((nx, ny))
                ans = max(ans, max([max(t[i]) for i in range(h)]))
    print(ans)

if __name__ == '__main__':
    main()