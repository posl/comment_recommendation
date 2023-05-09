def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    
    # 0: 未探索, 1: 探索済み, 2: 探索中
    state = [[0] * W for _ in range(H)]
    dist = [[-1] * W for _ in range(H)]
    
    def dfs(h, w, d):
        if state[h][w] == 2:
            return
        if state[h][w] == 1:
            if dist[h][w] <= d:
                return
            else:
                print(-1)
                exit()
        dist[h][w] = d
        state[h][w] = 2
        for dh, dw in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W:
                if S[nh][nw] == '.':
                    dfs(nh, nw, d + 1)
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W:
                    if S[nh][nw] == '.':
                        dfs(nh, nw, d + 1)
        state[h][w] = 1
    
    dfs(C_h - 1, C_w - 1, 0)
    print(dist[D_h - 1][D_w - 1])

if __name__ == '__main__':
    main()