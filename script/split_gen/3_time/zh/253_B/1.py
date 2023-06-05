def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    d = [[-1] * w for _ in range(h)]
    q = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                q.append((i, j))
                d[i][j] = 0
    while q:
        i, j = q.pop(0)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < h and 0 <= nj < w and d[ni][nj] == -1:
                d[ni][nj] = d[i][j] + 1
                q.append((ni, nj))
    print(max(max(row) for row in d))
