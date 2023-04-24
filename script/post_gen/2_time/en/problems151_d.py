Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            for di, dj in ((1, 0), (0, 1)):
                ni = i + di
                nj = j + dj
                if ni >= H or nj >= W:
                    continue
                if S[ni][nj] == '#':
                    continue
                ans = max(ans, abs(i - ni) + abs(j - nj))
    print(ans + 1)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            for k in range(i, H):
                for l in range(j, W):
                    if S[k][l] == "#":
                        continue
                    ans = max(ans, abs(i-k) + abs(j-l))
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if S[i][j] == "#" or S[k][l] == "#":
                        continue
                    dist = [[-1] * W for _ in range(H)]
                    dist[i][j] = 0
                    que = [(i, j)]
                    while que:
                        x, y = que.pop(0)
                        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if not (0 <= nx < H and 0 <= ny < W):
                                continue
                            if S[nx][ny] == "#":
                                continue
                            if dist[nx][ny] != -1:
                                continue
                            dist[nx][ny] = dist[x][y] + 1
                            que.append((nx, ny))
                    ans = max(ans, dist[k][l])
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if S[i][j] == S[k][l] == ".":
                        ans = max(ans, abs(i-k)+abs(j-l))
    print(ans)

=======
Suggestion 5

def main():
    H,W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                S[i][j] = 0
            else:
                S[i][j] = -1
    for i in range(H):
        for j in range(W):
            if S[i][j] != -1:
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    S[i][j] = S[i][j-1] + 1
                elif j == 0:
                    S[i][j] = S[i-1][j] + 1
                else:
                    S[i][j] = max(S[i-1][j], S[i][j-1]) + 1
    print(S[-1][-1])

main()

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    def bfs(sx, sy):
        dist = [[-1] * w for _ in range(h)]
        dist[sx][sy] = 0
        q = [(sx, sy)]
        while q:
            x, y = q.pop(0)
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + i, y + j
                if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '.' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        return dist

    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            dist = bfs(i, j)
            for k in range(h):
                for l in range(w):
                    if s[k][l] == '#':
                        continue
                    ans = max(ans, dist[k][l])
    print(ans)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    INF = 10**5
    dist = [[INF] * W for _ in range(H)]
    dist[0][0] = 0
    for h in range(H):
        for w in range(W):
            if h > 0 and S[h - 1][w] == '.' and S[h][w] == '.':
                dist[h][w] = min(dist[h][w], dist[h - 1][w] + 1)
            if w > 0 and S[h][w - 1] == '.' and S[h][w] == '.':
                dist[h][w] = min(dist[h][w], dist[h][w - 1] + 1)
    for h in range(H - 1, -1, -1):
        for w in range(W - 1, -1, -1):
            if h < H - 1 and S[h + 1][w] == '.' and S[h][w] == '.':
                dist[h][w] = min(dist[h][w], dist[h + 1][w] + 1)
            if w < W - 1 and S[h][w + 1] == '.' and S[h][w] == '.':
                dist[h][w] = min(dist[h][w], dist[h][w + 1] + 1)
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                ans = max(ans, dist[h][w])
    print(ans)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(list(input()))
    #print(S)

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            for k in range(H):
                for l in range(W):
                    if S[k][l] == '#':
                        continue
                    dist = [[-1 for m in range(W)] for n in range(H)]
                    dist[i][j] = 0
                    q = []
                    q.append([i, j])
                    while len(q) > 0:
                        x, y = q.pop(0)
                        if x > 0:
                            if S[x - 1][y] == '.' and dist[x - 1][y] == -1:
                                q.append([x - 1, y])
                                dist[x - 1][y] = dist[x][y] + 1
                        if x < H - 1:
                            if S[x + 1][y] == '.' and dist[x + 1][y] == -1:
                                q.append([x + 1, y])
                                dist[x + 1][y] = dist[x][y] + 1
                        if y > 0:
                            if S[x][y - 1] == '.' and dist[x][y - 1] == -1:
                                q.append([x, y - 1])
                                dist[x][y - 1] = dist[x][y] + 1
                        if y < W - 1:
                            if S[x][y + 1] == '.' and dist[x][y + 1] == -1:
                                q.append([x, y + 1])
                                dist[x][y + 1] = dist[x][y] + 1
                    #print(dist)
                    ans = max(ans, dist[k][l])

    print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    maze = [input() for _ in range(H)]
    #print(maze)
    dist = [[-1]*W for _ in range(H)]
    #print(dist)
    que = []
    for i in range(H):
        for j in range(W):
            if maze[i][j] == ".":
                que.append((i, j))
                dist[i][j] = 0
                break
    while que:
        i, j = que.pop(0)
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            if maze[ni][nj] == "#":
                continue
            if dist[ni][nj] != -1:
                continue
            dist[ni][nj] = dist[i][j] + 1
            que.append((ni, nj))
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, dist[i][j])
    print(ans)

=======
Suggestion 10

def main():
    H,W = map(int,input().split())
    S = []
    for i in range(H):
        S.append(list(input()))

    dist = [[-1]*W for i in range(H)]
    q = []
    q.append([0,0])
    dist[0][0] = 0
    while len(q) > 0:
        x,y = q.pop(0)
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < W and 0 <= ny < H and S[ny][nx] == "." and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append([nx,ny])

    print(dist[H-1][W-1] + 1)
