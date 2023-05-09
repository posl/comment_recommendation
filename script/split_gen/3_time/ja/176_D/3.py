def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    # スタート地点からの最短距離
    dist = [[-1] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    # スタート地点からの最短距離をBFSで求める
    from collections import deque
    q = deque()
    q.append((C_h, C_w))
    while q:
        h, w = q.popleft()
        # 移動A
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w] + 1
                q.append((nh, nw))
        # 移動B
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh = h + dh
                nw = w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w] + 1
                    q.append((nh, nw))
    print(dist[D_h][D_w])
