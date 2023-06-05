def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = [list(input()) for i in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    from collections import deque
    Q = deque()
    Q.append((C_h,C_w,0))
    dist = [[-1]*W for i in range(H)]
    dist[C_h][C_w] = 0
    while Q:
        i,j,d = Q.popleft()
        for i2,j2 in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist[i2][j2] == -1:
                dist[i2][j2] = d
                Q.appendleft((i2,j2,d))
        for i2 in range(i-2,i+3):
            for j2 in range(j-2,j+3):
                if not (0 <= i2 < H and 0 <= j2 < W):
                    continue
                if S[i2][j2] == '#':
                    continue
                if dist[i2][j2] == -1:
                    dist[i2][j2] = d + 1
                    Q.append((i2,j2,d+1))
    print(dist[D_h][D_w])

if __name__ == '__main__':
    main()