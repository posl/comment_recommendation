def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h, C_w, D_h, D_w = C_h-1, C_w-1, D_h-1, D_w-1
    dist = [[-1]*W for _ in range(H)]
    dist[C_h][C_w] = 0
    queue = [(C_h, C_w)]
    while queue:
        h, w = queue.pop(0)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h+dh, w+dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w]
                queue.append((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h+dh, w+dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w] + 1
                    queue.append((nh, nw))
    print(dist[D_h][D_w])

if __name__ == '__main__':
    main()