def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    # print(H, W)
    # print(C_h, C_w)
    # print(D_h, D_w)
    # print(S)
    # print(S[C_h][C_w])
    # print(S[D_h][D_w])
    import queue
    q = queue.Queue()
    q.put((C_h, C_w))
    dist = [[-1] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    while not q.empty():
        h, w = q.get()
        # print(h, w)
        # print(dist)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w] + 1
                q.put((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh = h + dh
                nw = w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w] + 1
                    q.put((nh, nw))
    print(dist[D_h][D_w])

if __name__ == '__main__':
    main()