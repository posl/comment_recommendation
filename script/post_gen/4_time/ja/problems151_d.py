Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                ans += 1
    print(ans - 1)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans += 1
    if ans == H * W:
        print(ans - 1)
    else:
        print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                S[h][w] = 0
            else:
                S[h][w] = -1
    for h in range(H):
        for w in range(W):
            if S[h][w] == -1:
                continue
            else:
                if h == 0 and w == 0:
                    continue
                elif h == 0:
                    if S[h][w-1] == -1:
                        S[h][w] = 0
                    else:
                        S[h][w] = S[h][w-1] + 1
                elif w == 0:
                    if S[h-1][w] == -1:
                        S[h][w] = 0
                    else:
                        S[h][w] = S[h-1][w] + 1
                else:
                    if S[h-1][w] == -1 and S[h][w-1] == -1:
                        S[h][w] = 0
                    elif S[h-1][w] == -1:
                        S[h][w] = S[h][w-1] + 1
                    elif S[h][w-1] == -1:
                        S[h][w] = S[h-1][w] + 1
                    else:
                        S[h][w] = min(S[h-1][w], S[h][w-1]) + 1
    print(S[H-1][W-1])

=======
Suggestion 4

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                ans = max(ans, calc(i, j, S, H, W))
    print(ans)

=======
Suggestion 5

def solve():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                ans += 1
    if ans == h * w:
        print(ans - 1)
    else:
        print(ans)

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(input())

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                ans += 1

    if ans == H+W-1:
        ans = ans - 1

    print(ans)

=======
Suggestion 7

def dfs(y, x, d):
    global ans
    ans = max(ans, d)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny < 0 or ny >= h or nx < 0 or nx >= w):
            continue
        if (s[ny][nx] == '#'):
            continue
        if (visited[ny][nx]):
            continue
        visited[ny][nx] = True
        dfs(ny, nx, d + 1)
        visited[ny][nx] = False

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(h):
    for j in range(w):
        if (s[i][j] == '#'):
            continue
        visited = [[False] * w for _ in range(h)]
        visited[i][j] = True
        dfs(i, j, 0)

print(ans)

=======
Suggestion 8

def bfs(maze, sx, sy, gx, gy):
    # 迷路のマスを4方向に移動するベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 各マスの最短距離を保持する配列
    dist = [[float("inf")] * W for i in range(H)]
    dist[sx][sy] = 0
    # 移動するマスを管理するキュー
    queue = []
    queue.append([sx, sy])

    while len(queue) > 0:
        p = queue.pop(0)
        if p[0] == gx and p[1] == gy:
            break
        # 移動するマスの周囲を探索
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            # 移動できるマスか判定
            if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != "#" and dist[nx][ny] == float("inf"):
                queue.append([nx, ny])
                dist[nx][ny] = dist[p[0]][p[1]] + 1

    return dist[gx][gy]

H, W = map(int, input().split())
maze = [list(input()) for i in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == "#":
            continue
        dist = bfs(maze, i, j, i, j)
        ans = max(ans, dist)
print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    # print(H, W, S)
    S = [[0 if S[i][j] == '.' else -1 for j in range(W)] for i in range(H)]
    # print(S)
    def bfs(i, j):
        # print(i, j)
        que = [(i, j)]
        while que:
            i, j = que.pop(0)
            # print(i, j)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i+di < H and 0 <= j+dj < W and S[i+di][j+dj] == 0:
                    S[i+di][j+dj] = S[i][j] + 1
                    que.append((i+di, j+dj))
    for i in range(H):
        for j in range(W):
            if S[i][j] == 0:
                bfs(i, j)
    print(max([max(S[i]) for i in range(H)]))
