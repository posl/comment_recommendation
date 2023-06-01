Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(i,j):
    if i == h - 1 and j == w - 1:
        return 1
    if visited[i][j]:
        return dp[i][j]
    visited[i][j] = True
    if i < h - 1 and maze[i+1][j] != '#':
        dp[i][j] += dfs(i+1,j)
    if j < w - 1 and maze[i][j+1] != '#':
        dp[i][j] += dfs(i,j+1)
    return dp[i][j]

h,w = map(int,input().split())
maze = [list(input()) for _ in range(h)]
visited = [[False for _ in range(w)] for _ in range(h)]
dp = [[0 for _ in range(w)] for _ in range(h)]
print(dfs(0,0))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    M = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if M[i][j] == '.':
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    print(dp[H - 1][W - 1])

=======
Suggestion 3

def dfs(x, y):
    global ans
    ans += 1
    field[x][y] = '#'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w and field[nx][ny]=='.':
            dfs(nx, ny)

h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0
dfs(0, 0)
print(ans)

=======
Suggestion 4

def max_walking(h, w, maze):
    # 以(i, j)为起点的最大步数
    # 从右下角开始，递归
    def max_walking_from(i, j):
        if i == h - 1 and j == w - 1:
            return 1
        if i >= h or j >= w:
            return 0
        if maze[i][j] == '#':
            return 0
        return max(max_walking_from(i + 1, j), max_walking_from(i, j + 1)) + 1

    return max_walking_from(0, 0)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == ".":
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    # 读入数据
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    # dp[i][j] 表示从(i, j)出发到达右下角的最大步数
    dp = [[0] * W for _ in range(H)]
    dp[H - 1][W - 1] = 1
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if i == H - 1 and j == W - 1:
                continue
            if C[i][j] == '#':
                continue
            if i == H - 1:
                dp[i][j] = dp[i][j + 1]
            elif j == W - 1:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
    print(dp[0][0])

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1 if grid[0][0] == '.' else 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    print(dp[-1][-1])

=======
Suggestion 8

def main():
    h,w = map(int,input().split())
    c = [input() for _ in range(h)]
    
    #print(c)
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == ".":
                ans += 1

    print(ans)

=======
Suggestion 9

def dfs(i,j):
    if i==h-1 and j==w-1:
        return 1
    if i>h-1 or j>w-1:
        return 0
    if grid[i][j]==1:
        return 0
    grid[i][j]=1
    return dfs(i+1,j)+dfs(i,j+1)

h,w=map(int,input().split())
grid=[[0]*w for _ in range(h)]
for i in range(h):
    s=input()
    for j in range(w):
        if s[j]=='#':
            grid[i][j]=1
print(dfs(0,0))

=======
Suggestion 10

def dfs(x, y):
    if x == h - 1 and y == w - 1:
        return 1
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == '#':
        return 0
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = dfs(x + 1, y) + dfs(x, y + 1)
    return dp[x][y]

h, w = map(int, input().split())
c = [input() for _ in range(h)]
dp = [[-1] * w for _ in range(h)]
print(dfs(0, 0))
