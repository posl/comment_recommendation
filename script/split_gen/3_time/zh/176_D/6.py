def main():
    h, w = map(int, input().split())
    c_h, c_w = map(int, input().split())
    d_h, d_w = map(int, input().split())
    s = [input() for _ in range(h)]
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    dist = [[float('inf')] * w for _ in range(h)]
    dist[c_h][c_w] = 0
    queue = [(c_h, c_w)]
    while queue:
        i, j = queue.pop(0)
        for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if not (0 <= i2 < h and 0 <= j2 < w): continue
            if s[i2][j2] == '#': continue
            if dist[i2][j2] <= dist[i][j]: continue
            dist[i2][j2] = dist[i][j]
            queue.append((i2, j2))
        for i2 in range(i - 2, i + 3):
            for j2 in range(j - 2, j + 3):
                if not (0 <= i2 < h and 0 <= j2 < w): continue
                if s[i2][j2] == '#': continue
                if dist[i2][j2] <= dist[i][j] + 1: continue
                dist[i2][j2] = dist[i][j] + 1
                queue.append((i2, j2))
    if dist[d_h][d_w] == float('inf'):
        print(-1)
    else:
        print(dist[d_h][d_w])
