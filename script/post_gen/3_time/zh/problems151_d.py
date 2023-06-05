Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                t = [[-1] * w for _ in range(h)]
                t[i][j] = 0
                q = [(i, j)]
                while q:
                    y, x = q.pop(0)
                    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < h and 0 <= nx < w and s[ny][nx] == "." and t[ny][nx] == -1:
                            t[ny][nx] = t[y][x] + 1
                            q.append((ny, nx))
                ans = max(ans, max([max(u) for u in t]))
    print(ans)
main()

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                t = [[-1] * w for _ in range(h)]
                t[i][j] = 0
                q = [(i, j)]
                for x, y in q:
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '.' and t[nx][ny] < 0:
                            t[nx][ny] = t[x][y] + 1
                            q.append((nx, ny))
                ans = max(ans, max([max(t[i]) for i in range(h)]))
    print(ans)

=======
Suggestion 3

def main():
    H,W = map(int,input().split())
    S = [list(input()) for i in range(H)]

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                #print(i,j)
                #print(S[i][j])
                #print(S[i][j+1])
                #print(S[i][j-1])
                #print(S[i+1][j])
                #print(S[i-1][j])
                if i == 0:
                    if j == 0:
                        if S[i][j+1] == '.':
                            ans += 1
                        if S[i+1][j] == '.':
                            ans += 1
                    elif j == W-1:
                        if S[i][j-1] == '.':
                            ans += 1
                        if S[i+1][j] == '.':
                            ans += 1
                    else:
                        if S[i][j+1] == '.':
                            ans += 1
                        if S[i][j-1] == '.':
                            ans += 1
                        if S[i+1][j] == '.':
                            ans += 1
                elif i == H-1:
                    if j == 0:
                        if S[i][j+1] == '.':
                            ans += 1
                        if S[i-1][j] == '.':
                            ans += 1
                    elif j == W-1:
                        if S[i][j-1] == '.':
                            ans += 1
                        if S[i-1][j] == '.':
                            ans += 1
                    else:
                        if S[i][j+1] == '.':
                            ans += 1
                        if S[i][j-1] == '.':
                            ans += 1
                        if S[i-1][j] == '.':
                            ans += 1
                else:
                    if j == 0:
                        if S[i][j+1] == '.':
                            ans += 1
                        if S[i+1][j] == '.':
                            ans += 1
                        if S[i-1][j] == '.':
                            ans += 1
                    elif j == W-1:
                        if S[i][j-1] == '.':
                            ans +=

=======
Suggestion 4

def dfs(h,w):
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                dfs(i,j)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                t = [[-1] * w for _ in range(h)]
                t[i][j] = 0
                q = [(i, j)]
                while q:
                    y, x = q.pop(0)
                    for ny, nx in ((y + 1, x), (y, x + 1), (y - 1, x), (y, x - 1)):
                        if 0 <= ny < h and 0 <= nx < w and s[ny][nx] == '.' and t[ny][nx] == -1:
                            t[ny][nx] = t[y][x] + 1
                            q.append((ny, nx))
                ans = max(ans, max([max(l) for l in t]))
    print(ans)

=======
Suggestion 6

def dfs(x, y, d):
    global ans
    ans = max(ans, d)
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '.' and not used[nx][ny]:
            used[nx][ny] = True
            dfs(nx, ny, d + 1)
            used[nx][ny] = False


h, w = map(int, input().split())
s = [input() for _ in range(h)]
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            used = [[False] * w for _ in range(h)]
            used[i][j] = True
            dfs(i, j, 0)
print(ans)

=======
Suggestion 7

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    # 从每个点开始，寻找到其他每个点的最短距离
    from collections import deque
    def bfs(sy, sx):
        dist = [[-1] * W for _ in range(H)]
        dist[sy][sx] = 0
        q = deque([(sy, sx)])
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < H and 0 <= nx < W): continue
                if S[ny][nx] == '#': continue
                if dist[ny][nx] != -1: continue
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
        return dist

    dists = [bfs(sy, sx) for sy in range(H) for sx in range(W)]

    ans = 0
    for i in range(H * W):
        for j in range(i + 1, H * W):
            if dists[i // W][i % W][j // W][j % W] == -1: continue
            ans = max(ans, dists[i // W][i % W][j // W][j % W])
    print(ans)

solve()

=======
Suggestion 8

def maze():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                S[i][j] = 0
            else:
                S[i][j] = -1
    for i in range(H):
        for j in range(W):
            if S[i][j] == 0:
                S[i][j] = 1
                for k in range(1, H):
                    if i + k < H and S[i + k][j] != -1:
                        S[i + k][j] = S[i][j] + 1
                    else:
                        break
                for k in range(1, H):
                    if i - k >= 0 and S[i - k][j] != -1:
                        S[i - k][j] = S[i][j] + 1
                    else:
                        break
                for k in range(1, W):
                    if j + k < W and S[i][j + k] != -1:
                        S[i][j + k] = S[i][j] + 1
                    else:
                        break
                for k in range(1, W):
                    if j - k >= 0 and S[i][j - k] != -1:
                        S[i][j - k] = S[i][j] + 1
                    else:
                        break
                ans = max(ans, S[i][j])
    print(ans)

maze()

=======
Suggestion 9

def dfs(x,y):
    global max_depth
    global depth
    global visited
    global goal_x
    global goal_y
    if x == goal_x and y == goal_y:
        max_depth = max(max_depth,depth)
        return
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<H and 0<=ny<W and visited[nx][ny] == False and maze[nx][ny] == '.':
            depth += 1
            dfs(nx,ny)
            depth -= 1
    visited[x][y] = False

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                t = 0
                for k in range(h):
                    if s[k][j] == '#':
                        break
                    t += 1
                for k in range(j+1, w):
                    if s[i][k] == '#':
                        break
                    t += 1
                for k in range(i-1, -1, -1):
                    if s[k][j] == '#':
                        break
                    t += 1
                for k in range(j-1, -1, -1):
                    if s[i][k] == '#':
                        break
                    t += 1
                ans = max(ans, t-3)
    print(ans)
