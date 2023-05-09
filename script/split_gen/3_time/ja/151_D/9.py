def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 道のマスの数をカウント
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                cnt += 1
    # スタートとゴールのマスを決める
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                start = (i, j)
                break
        else:
            continue
        break
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if S[i][j] == '.':
                goal = (i, j)
                break
        else:
            continue
        break
    # スタートからゴールまでの最短経路を求める
    from collections import deque
    dist = [[-1] * W for _ in range(H)]
    dist[start[0]][start[1]] = 0
    q = deque([start])
    while q:
        p = q.popleft()
        if p == goal:
            break
        for x, y in ((p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)):
            if 0 <= x < H and 0 <= y < W and S[x][y] == '.' and dist[x][y] == -1:
                dist[x][y] = dist[p[0]][p[1]] + 1
                q.append((x, y))
    print(cnt - dist[goal[0]][goal[1]] - 1)
