def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    from collections import deque
    q = deque()
    q.append((C_h, C_w, 0))
    visited = [[False] * W for _ in range(H)]
    visited[C_h][C_w] = True
    while q:
        i, j, cost = q.popleft()
        if i == D_h and j == D_w:
            print(cost)
            return
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            if visited[ni][nj]:
                continue
            if S[ni][nj] == '#':
                continue
            q.append((ni, nj, cost))
            visited[ni][nj] = True
        for di in range(-2, 3):
            for dj in range(-2, 3):
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    continue
                if visited[ni][nj]:
                    continue
                if S[ni][nj] == '#':
                    continue
                q.append((ni, nj, cost + 1))
                visited[ni][nj] = True
    print(-1)
