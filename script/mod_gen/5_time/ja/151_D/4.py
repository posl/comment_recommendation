def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            d = [[-1] * w for _ in range(h)]
            d[i][j] = 0
            q = [(i, j)]
            while q:
                y, x = q.pop(0)
                for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ny, nx = y + dy, x + dx
                    if ny < 0 or nx < 0 or ny >= h or nx >= w:
                        continue
                    if s[ny][nx] == '#':
                        continue
                    if d[ny][nx] == -1:
                        d[ny][nx] = d[y][x] + 1
                        q.append((ny, nx))
            ans = max(ans, max([max(l) for l in d]))
    print(ans)
main()

if __name__ == '__main__':
    main()