def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h, C_w, D_h, D_w = C_h-1, C_w-1, D_h-1, D_w-1
    from collections import deque
    q = deque([(C_h, C_w, 0)])
    d = [[-1]*W for _ in range(H)]
    d[C_h][C_w] = 0
    while q:
        i, j, k = q.popleft()
        if i == D_h and j == D_w:
            print(k)
            return
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '.' and d[ni][nj] == -1:
                d[ni][nj] = k
                q.appendleft((ni, nj, k))
        for di in range(-2, 3):
            for dj in range(-2, 3):
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '.' and d[ni][nj] == -1:
                    d[ni][nj] = k + 1
                    q.append((ni, nj, k + 1))
    print(-1)

if __name__ == '__main__':
    main()