def main():
    #input
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    #process
    import collections
    from heapq import heappop, heappush
    INF = 10**9
    dist = [[INF]*W for _ in range(H)]
    dist[C_h-1][C_w-1] = 0
    que = [(0, C_h-1, C_w-1)]
    while que:
        d, h, w = heappop(que)
        if dist[h][w] < d:
            continue
        for dh, dw in ((0,1),(0,-1),(1,0),(-1,0)):
            if 0<=h+dh<H and 0<=w+dw<W and S[h+dh][w+dw]=='.' and dist[h+dh][w+dw]>d:
                dist[h+dh][w+dw] = d
                heappush(que, (d, h+dh, w+dw))
        for dh in range(-2,3):
            for dw in range(-2,3):
                if 0<=h+dh<H and 0<=w+dw<W and S[h+dh][w+dw]=='.' and dist[h+dh][w+dw]>d+1:
                    dist[h+dh][w+dw] = d+1
                    heappush(que, (d+1, h+dh, w+dw))
    #output
    if dist[D_h-1][D_w-1]==INF:
        print(-1)
    else:
        print(dist[D_h-1][D_w-1])

if __name__ == '__main__':
    main()