def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            for k in range(H):
                for l in range(W):
                    if S[k][l] == "#":
                        continue
                    dist = [[-1]*W for _ in range(H)]
                    dist[i][j] = 0
                    Q = [(i, j)]
                    while Q:
                        x, y = Q.pop()
                        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            nx, ny = x + dx, y + dy
                            if not (0 <= nx < H and 0 <= ny < W):
                                continue
                            if S[nx][ny] == "#":
                                continue
                            if dist[nx][ny] != -1:
                                continue
                            dist[nx][ny] = dist[x][y] + 1
                            Q.append((nx, ny))
                    ans = max(ans, dist[k][l])
    print(ans)

if __name__ == '__main__':
    main()