def solve():
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    ch -= 1
    cw -= 1
    dh -= 1
    dw -= 1
    s = [input() for _ in range(h)]
    d = [[-1] * w for _ in range(h)]
    d[ch][cw] = 0
    q = []
    q.append((ch, cw))
    while q:
        i, j = q.pop(0)
        for i2 in range(i - 2, i + 3):
            for j2 in range(j - 2, j + 3):
                if not (0 <= i2 < h and 0 <= j2 < w):
                    continue
                if s[i2][j2] == '#':
                    continue
                if d[i2][j2] != -1:
                    continue
                if abs(i2 - i) + abs(j2 - j) == 1:
                    d[i2][j2] = d[i][j]
                    q.append((i2, j2))
                else:
                    d[i2][j2] = d[i][j] + 1
                    q.append((i2, j2))
    print(d[dh][dw])
solve()
