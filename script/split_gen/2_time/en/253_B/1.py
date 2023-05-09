def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                start = (i, j)
            elif S[i][j] == 'x':
                goal = (i, j)
    from collections import deque
    Q = deque([start])
    dist = [[-1] * W for _ in range(H)]
    dist[start[0]][start[1]] = 0
    while Q:
        i, j = Q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and dist[ni][nj] == -1 and S[ni][nj] != 'x':
                dist[ni][nj] = dist[i][j] + 1
                Q.append((ni, nj))
    print(dist[goal[0]][goal[1]])
main()
