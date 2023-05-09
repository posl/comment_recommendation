def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(input())
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    dist = [[-1]*W for _ in range(H)]
    dist[C_h][C_w] = 0
    Q = [(C_h,C_w)]
    while Q:
        h,w = Q.pop(0)
        for dh,dw in [(0,1),(0,-1),(1,0),(-1,0)]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w]
                Q.append((nh,nw))
        for dh in range(-2,3):
            for dw in range(-2,3):
                nh = h + dh
                nw = w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w] + 1
                    Q.append((nh,nw))
    print(dist[D_h][D_w])

if __name__ == '__main__':
    main()