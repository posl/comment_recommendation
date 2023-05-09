def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    
    # (C_h, C_w) から (D_h, D_w) への最短距離を求める
    # 距離の初期化
    INF = 10 ** 9
    dist = [[INF] * W for _ in range(H)]
    dist[C_h-1][C_w-1] = 0
    
    # 1回目のBFS
    # 移動Aのみで到達可能なマスを全てキューに入れる
    from collections import deque
    q = deque()
    q.append((C_h-1, C_w-1))
    while q:
        h, w = q.popleft()
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dh += h
            dw += w
            if 0 <= dh < H and 0 <= dw < W and S[dh][dw] == '.' and dist[dh][dw] == INF:
                dist[dh][dw] = dist[h][w] + 1
                q.append((dh, dw))
    
    # 2回目のBFS
    # 移動Aのみで到達可能なマスから、移動Bで到達可能なマスを全てキューに入れる
    q = deque()
    for h in range(H):
        for w in range(W):
            if dist[h][w] <= 2:
                q.append((h, w))
                dist[h][w] = 0
    while q:
        h, w = q.popleft()
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                dh += h
                dw += w
                if 0 <= dh < H and 0 <= dw < W and S[dh][dw] == '.' and dist[dh][dw] == INF:
                    dist[dh][dw

if __name__ == '__main__':
    main()