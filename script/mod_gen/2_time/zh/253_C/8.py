def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 计算棋子之间的最短距离
    dist = [[float('inf')] * W for _ in range(H)]
    # 棋子的坐标
    q = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                dist[i][j] = 0
                q.append((i, j))
    
    while q:
        i, j = q.pop(0)
        for i2, j2 in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if dist[i2][j2] != float('inf'):
                continue
            dist[i2][j2] = dist[i][j] + 1
            q.append((i2, j2))
    
    res = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                continue
            res = max(res, dist[i][j])
    
    print(res)

if __name__ == '__main__':
    solve()