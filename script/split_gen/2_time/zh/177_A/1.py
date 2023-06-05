def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    from collections import deque
    que = deque()
    que.append((C_h, C_w))
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    dist[C_h][C_w] = 0
    while que:
        cur_h, cur_w = que.popleft()
        for dh, dw in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            next_h = cur_h + dh
            next_w = cur_w + dw
            if 0 <= next_h < H and 0 <= next_w < W and S[next_h][next_w] == '.' and dist[next_h][next_w] == -1:
                dist[next_h][next_w] = dist[cur_h][cur_w]
                que.appendleft((next_h, next_w))
        for i in range(-2, 3):
            for j in range(-2, 3):
                next_h = cur_h + i
                next_w = cur_w + j
                if 0 <= next_h < H and 0 <= next_w < W and S[next_h][next_w] == '.' and dist[next_h][next_w] == -1:
                    dist[next_h][next_w] = dist[cur_h][cur_w] + 1
                    que.append((next_h, next_w))
    print(dist[D_h][D_w])
