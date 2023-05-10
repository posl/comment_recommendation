def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for i in range(H)]
    def bfs(S, C_h, C_w, D_h, D_w):
        from collections import deque
        q = deque()
        q.append((C_h-1, C_w-1))
        dist = [[float('inf')] * W for i in range(H)]
        dist[C_h-1][C_w-1] = 0
        while q:
            i, j = q.popleft()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if not (0 <= ni < H and 0 <= nj < W):
                    continue
                if S[ni][nj] == '#':
                    continue
                if dist[ni][nj] > dist[i][j]:
                    dist[ni][nj] = dist[i][j]
                    q.appendleft((ni, nj))
            for di in range(-2, 3):
                for dj in range(-2, 3):
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < H and 0 <= nj < W):
                        continue
                    if S[ni][nj] == '#':
                        continue
                    if dist[ni][nj] > dist[i][j] + 1:
                        dist[ni][nj] = dist[i][j] + 1
                        q.append((ni, nj))
        return dist[D_h-1][D_w-1]
    ans = bfs(S, C_h, C_w, D_h, D_w)
    print(ans)

if __name__ == '__main__':
    main()