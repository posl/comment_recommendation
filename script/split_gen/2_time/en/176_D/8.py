def main():
    import sys
    from collections import deque
    H,W = map(int,sys.stdin.readline().split())
    C_h,C_w = map(int,sys.stdin.readline().split())
    D_h,D_w = map(int,sys.stdin.readline().split())
    S = [sys.stdin.readline().rstrip() for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    visited[C_h-1][C_w-1] = True
    que = deque()
    que.append((C_h-1,C_w-1,0))
    while que:
        h,w,cnt = que.popleft()
        if h == D_h-1 and w == D_w-1:
            print(cnt)
            return
        for dh,dw in ((0,1),(1,0),(-1,0),(0,-1)):
            nh,nw = h+dh,w+dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and not visited[nh][nw]:
                visited[nh][nw] = True
                que.append((nh,nw,cnt))
        for dh in range(-2,3):
            for dw in range(-2,3):
                nh,nw = h+dh,w+dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and not visited[nh][nw]:
                    visited[nh][nw] = True
                    que.append((nh,nw,cnt+1))
    print(-1)
