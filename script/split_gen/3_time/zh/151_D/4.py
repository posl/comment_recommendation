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
                while q:
                    y, x = q.pop(0)
                    for ny, nx in ((y + 1, x), (y, x + 1), (y - 1, x), (y, x - 1)):
                        if 0 <= ny < h and 0 <= nx < w and s[ny][nx] == '.' and t[ny][nx] == -1:
                            t[ny][nx] = t[y][x] + 1
                            q.append((ny, nx))
                ans = max(ans, max([max(l) for l in t]))
    print(ans)
