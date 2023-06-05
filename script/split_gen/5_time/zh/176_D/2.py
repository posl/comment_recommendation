def main():
    h,w = map(int,input().split())
    c_h,c_w = map(int,input().split())
    d_h,d_w = map(int,input().split())
    s = [input() for i in range(h)]
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    #print(h,w,c_h,c_w,d_h,d_w,s)
    visited = [[False]*w for i in range(h)]
    visited[c_h][c_w] = True
    q = []
    q.append((c_h,c_w,0))
    while len(q) > 0:
        (ch,cw,step) = q.pop(0)
        #print(ch,cw,step)
        if ch == d_h and cw == d_w:
            print(step)
            return
        for (dh,dw) in [(0,1),(0,-1),(1,0),(-1,0)]:
            nh = ch + dh
            nw = cw + dw
            if nh >= 0 and nh < h and nw >= 0 and nw < w and s[nh][nw] == '.' and visited[nh][nw] == False:
                visited[nh][nw] = True
                q.append((nh,nw,step))
        for dh in range(-2,3):
            for dw in range(-2,3):
                nh = ch + dh
                nw = cw + dw
                if nh >= 0 and nh < h and nw >= 0 and nw < w and s[nh][nw] == '.' and visited[nh][nw] == False:
                    visited[nh][nw] = True
                    q.append((nh,nw,step+1))
    print(-1)
