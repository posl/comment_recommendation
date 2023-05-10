def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    x = [xy[i][0] for i in range(n)]
    y = [xy[i][1] for i in range(n)]
    m = 40
    d = [0] * m
    w = [[''] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            dx = x[j] - x[i]
            dy = y[j] - y[i]
            if dx >= 0 and dy >= 0:
                w[i][j] = 'R' * dx + 'U' * dy
            elif dx >= 0 and dy < 0:
                w[i][j] = 'R' * dx + 'D' * (-dy)
            elif dx < 0 and dy >= 0:
                w[i][j] = 'L' * (-dx) + 'U' * dy
            else:
                w[i][j] = 'L' * (-dx) + 'D' * (-dy)
    for i in range(m):
        d[i] = 10 ** 12
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d[i] = min(d[i], len(w[i][j]))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if len(w[i][j]) == d[i]:
                w[i][j] = w[i][j][:-1]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if len(w[i][j]) < d[i]:
                w[i][j] += w[j][i]
                w[i][j] += w[i][j][0] * (d[i] - len(w[i][j]))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if len(w[i][j]) > d[i]:
                w[i][j] = w[i][j][:d[i]]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
