def main():
    #入力
    H,W = map(int,input().split())
    Ch,Cw = map(int,input().split())
    Dh,Dw = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    #print(H,W,Ch,Cw,Dh,Dw,S)
    #初期化
    INF = 10**9
    dist = [[INF]*W for _ in range(H)]
    #bfs
    import collections
    q = collections.deque()
    q.append((Ch-1,Cw-1))
    dist[Ch-1][Cw-1] = 0
    while q:
        h,w = q.popleft()
        #print(h,w)
        #移動A
        for dh,dw in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0<=h+dh<H and 0<=w+dw<W and S[h+dh][w+dw]=="." and dist[h][w]+1<dist[h+dh][w+dw]:
                dist[h+dh][w+dw] = dist[h][w]+1
                q.append((h+dh,w+dw))
        #移動B
        for dh in range(-2,3):
            for dw in range(-2,3):
                if 0<=h+dh<H and 0<=w+dw<W and S[h+dh][w+dw]=="." and dist[h][w]+1<dist[h+dh][w+dw]:
                    dist[h+dh][w+dw] = dist[h][w]+1
                    q.append((h+dh,w+dw))
    if dist[Dh-1][Dw-1]==INF:
        print(-1)
    else:
        print(dist[Dh-1][Dw-1])
