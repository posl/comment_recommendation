def main():
    from collections import deque
    import sys
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    dh = [0, 1, 0, -1]
    dw = [1, 0, -1, 0]
    q = deque()
    q.append((C_h-1, C_w-1, 0))
    while q:
        h, w, cnt = q.popleft()
        if h == D_h-1 and w == D_w-1:
            print(cnt)
            sys.exit()
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.':
                S[nh][nw] = '#'
                q.append((nh, nw, cnt))
        for i in range(-2, 3):
            for j in range(-2, 3):
                nh = h + i
                nw = w + j
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.':
                    S[nh][nw] = '#'
                    q.append((nh, nw, cnt+1))
    print(-1)

if __name__ == '__main__':
    main()