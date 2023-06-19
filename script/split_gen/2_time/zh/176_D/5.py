def problem176_d():
    H,W = map(int, input().split())
    C_h,C_w = map(int, input().split())
    D_h,D_w = map(int, input().split())
    S = [list(input()) for i in range(H)]
    C_h,C_w,D_h,D_w = C_h-1,C_w-1,D_h-1,D_w-1
    dist = [[-1]*W for i in range(H)]
    dist[C_h][C_w] = 0
    q = [(C_h,C_w)]
    while q:
        h,w = q.pop(0)
        for dh,dw in [(1,0),(0,1),(-1,0),(0,-1)]:
            nh,nw = h+dh,w+dw
            if nh<0 or nh>=H or nw<0 or nw>=W: continue
            if S[nh][nw] == '#': continue
            if dist[nh][nw] != -1: continue
            dist[nh][nw] = dist[h][w]
            q.append((nh,nw))
        for dh in range(-2,3):
            for dw in range(-2,3):
                nh,nw = h+dh,w+dw
                if nh<0 or nh>=H or nw<0 or nw>=W: continue
                if S[nh][nw] == '#': continue
                if dist[nh][nw] != -1: continue
                dist[nh][nw] = dist[h][w]+1
                q.append((nh,nw))
    print(dist[D_h][D_w])
