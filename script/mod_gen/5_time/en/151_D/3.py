def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                #print(i,j)
                dist = [[-1] * W for _ in range(H)]
                dist[i][j] = 0
                q = [(i,j)]
                while q:
                    x, y = q.pop(0)
                    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.' and dist[nx][ny] == -1:
                            dist[nx][ny] = dist[x][y] + 1
                            q.append((nx, ny))
                ans = max(ans, max([max(d) for d in dist]))
    print(ans)
solve()

if __name__ == '__main__':
    solve()