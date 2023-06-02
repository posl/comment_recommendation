Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h,w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                cnt += 1
    if cnt == h*w:
        print(h+w-1)
    else:
        print(h+w-3)

=======
Suggestion 2

def bfs(S, start, goal):
    INF = 10 ** 9
    H, W = len(S), len(S[0])
    dist = [[INF] * W for _ in range(H)]
    dist[start[0]][start[1]] = 0
    que = []
    que.append(start)
    while que:
        y, x = que.pop(0)
        for dy, dx in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            if S[ny][nx] == '#':
                continue
            if dist[ny][nx] != INF:
                continue
            dist[ny][nx] = dist[y][x] + 1
            que.append((ny, nx))
    return dist[goal[0]][goal[1]]

H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        ans = max(ans, bfs(S, (i, j), (i, j)))
print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for si in S:
        ans += si.count('.')
    if ans == H + W - 1:
        ans -= 1
    print(ans)

=======
Suggestion 4

def count_dis(l):
    l = l.split('#')
    return max([len(i) for i in l])

h, w = map(int, input().split())
l = []
for i in range(h):
    l.append(input())
l = list(filter(lambda x: '#' not in x, l))
print(count_dis(''.join(l)) + len(l) - 1)

=======
Suggestion 5

def dfs(start, goal, maze, visited, count):
    if start[0] == goal[0] and start[1] == goal[1]:
        return count
    else:
        visited[start[0]][start[1]] = 1
        if start[0] > 0 and maze[start[0]-1][start[1]] == '.' and visited[start[0]-1][start[1]] == 0:
            count = dfs([start[0]-1, start[1]], goal, maze, visited, count+1)
        if start[1] > 0 and maze[start[0]][start[1]-1] == '.' and visited[start[0]][start[1]-1] == 0:
            count = dfs([start[0], start[1]-1], goal, maze, visited, count+1)
        if start[0] < len(maze)-1 and maze[start[0]+1][start[1]] == '.' and visited[start[0]+1][start[1]] == 0:
            count = dfs([start[0]+1, start[1]], goal, maze, visited, count+1)
        if start[1] < len(maze[0])-1 and maze[start[0]][start[1]+1] == '.' and visited[start[0]][start[1]+1] == 0:
            count = dfs([start[0], start[1]+1], goal, maze, visited, count+1)
    return count

=======
Suggestion 6

def main():
    r,c = map(int, input().split())
    S = []
    for i in range(r):
        S.append(list(input()))
    # print(S)
    max = 0
    for i in range(r):
        for j in range(c):
            if S[i][j] == '.':
                tmp = 0
                for k in range(i+1, r):
                    if S[k][j] == '#':
                        break
                    else:
                        tmp += 1
                for k in range(i-1, -1, -1):
                    if S[k][j] == '#':
                        break
                    else:
                        tmp += 1
                for k in range(j+1, c):
                    if S[i][k] == '#':
                        break
                    else:
                        tmp += 1
                for k in range(j-1, -1, -1):
                    if S[i][k] == '#':
                        break
                    else:
                        tmp += 1
                if tmp > max:
                    max = tmp
    print(max+1)

=======
Suggestion 7

def dfs(x,y):
    global maxv
    if x < 0 or x >= h or y < 0 or y >= w:
        return
    if maze[x][y] == '#':
        return
    if maxv < dist[x][y]:
        maxv = dist[x][y]
    if dist[x][y] != -1:
        return
    dist[x][y] = dist[px][py] + 1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    dist[x][y] = -1

h,w = map(int,input().split())
maze = [input() for i in range(h)]
dist = [[-1]*w for i in range(h)]
maxv = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            px = i
            py = j
            dfs(i,j)
print(maxv)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                ans = max(ans, dfs(S, h, w))
    print(ans)

=======
Suggestion 9

def main():
    h,w = map(int,input().split())
    s = [list(input()) for _ in range(h)]

    def dfs(i,j):
        s[i][j] = "#"
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = i+dx,j+dy
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if s[ni][nj] == "#":
                continue
            dfs(ni,nj)
        s[i][j] = "."

    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue
            t = [[0]*w for _ in range(h)]
            t[i][j] = 1
            q = [(i,j)]
            while q:
                ni,nj = q.pop(0)
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    x,y = ni+dx,nj+dy
                    if x < 0 or x >= h or y < 0 or y >= w:
                        continue
                    if s[x][y] == "#":
                        continue
                    if t[x][y] > 0:
                        continue
                    t[x][y] = t[ni][nj] + 1
                    q.append((x,y))
            for k in range(h):
                for l in range(w):
                    if s[k][l] == "#":
                        continue
                    ans = max(ans,t[k][l]-1)
    print(ans)

=======
Suggestion 10

def dfs(x,y):
    visited[x][y] = 1
    for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
        nx,ny = x+dx,y+dy
        if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.' and visited[nx][ny] == 0:
            dfs(nx,ny)
    return

H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]

res = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            visited = [[0]*W for _ in range(H)]
            dfs(i,j)
            res = max(res,sum([sum(visited[i]) for i in range(H)]))
print(res)
