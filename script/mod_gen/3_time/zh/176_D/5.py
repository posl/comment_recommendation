def main():
    h, w = map(int, input().split())
    c_h, c_w = map(int, input().split())
    d_h, d_w = map(int, input().split())
    s = [input() for _ in range(h)]
    # 距离を管理する配列
    dist = [[-1] * w for _ in range(h)]
    # 幅優先探索
    q = []
    q.append((c_h - 1, c_w - 1))
    dist[c_h - 1][c_w - 1] = 0
    while len(q) > 0:
        i, j = q.pop(0)
        for i2, j2 in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
            if not (0 <= i2 < h and 0 <= j2 < w):
                continue
            if s[i2][j2] == '#':
                continue
            if dist[i2][j2] == -1:
                dist[i2][j2] = dist[i][j] + 1
                q.append((i2, j2))
    # 答え
    ans = dist[d_h - 1][d_w - 1]
    print(ans)

if __name__ == '__main__':
    main()