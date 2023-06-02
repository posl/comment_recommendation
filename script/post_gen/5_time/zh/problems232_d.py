Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == '.':
                ans += 1
    print(ans)

=======
Suggestion 2

def get_max_count(x, y, H, W, C):
    if x == H or y == W:
        return 0
    if C[x][y] == '#':
        return 0
    return max(get_max_count(x+1, y, H, W, C), get_max_count(x, y+1, H, W, C)) + 1

H, W = map(int, input().split())
C = []
for i in range(H):
    C.append(list(input()))

print(get_max_count(0, 0, H, W, C))

=======
Suggestion 3

def dfs(x,y):
    global ans
    if x == H-1 and y == W-1:
        ans += 1
        return
    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != '#':
                dfs(nx,ny)
        return

H,W = map(int,input().split())
maze = [input() for i in range(H)]
ans = 0
dx = [0,1]
dy = [1,0]
dfs(0,0)
print(ans)

=======
Suggestion 4

def solve(h, w, s):
    #print(h, w, s)
    res = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            t = 0
            for k in range(i, h):
                if s[k][j] == '#':
                    break
                t += 1
            res = max(res, t)
            t = 0
            for k in range(j, w):
                if s[i][k] == '#':
                    break
                t += 1
            res = max(res, t)
    return res

=======
Suggestion 5

def dfs(x,y):
    if x == h-1 and y == w-1:
        return 1
    if x >= h or y >= w:
        return 0
    if d[x][y] != -1:
        return d[x][y]
    if s[x][y] == '#':
        return 0
    d[x][y] = dfs(x+1,y) + dfs(x,y+1)
    return d[x][y]

h,w = map(int,input().split())
s = [input() for i in range(h)]
d = [[-1]*w for i in range(h)]
print(dfs(0,0))

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def dfs(i, j):
    global ans
    if i == h - 1 and j == w - 1:
        ans += 1
        return
    if i + 1 < h and maze[i + 1][j] == '.':
        dfs(i + 1, j)
    if j + 1 < w and maze[i][j + 1] == '.':
        dfs(i, j + 1)

h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
ans = 0
dfs(0, 0)
print(ans)

=======
Suggestion 8

def main():
    #input
    h, w = map(int, input().split())
    maze = [list(input()) for i in range(h)]

    #init
    dp = [[0 for j in range(w)] for i in range(h)]
    dp[0][0] = 1

    #loop
    for i in range(h):
        for j in range(w):
            if maze[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % 1000000007
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % 1000000007

    #output
    print(dp[h-1][w-1])

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == '.':
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    print(dp[H-1][W-1]%1000000007)

=======
Suggestion 10

def dfs(i, j):
    if i == h-1 and j == w-1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]

    res = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < h and 0 <= nj < w:
            if c[ni][nj] == ".":
                res += dfs(ni, nj)
    dp[i][j] = res
    return res

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
dp = [[-1]*w for _ in range(h)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
print(dfs(0, 0))
