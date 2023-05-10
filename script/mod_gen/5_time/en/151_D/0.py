def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                from collections import deque
                d = [[-1] * w for _ in range(h)]
                d[i][j] = 0
                q = deque([(i, j)])
                while q:
                    y, x = q.popleft()
                    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < h and 0 <= nx < w and s[ny][nx] == "." and d[ny][nx] == -1:
                            d[ny][nx] = d[y][x] + 1
                            q.append((ny, nx))
                ans = max(ans, max(map(max, d)))
    print(ans)

if __name__ == '__main__':
    main()