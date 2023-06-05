Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    maze = [input() for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if maze[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    print(dp[-1][-1])

=======
Suggestion 2

def get_max_count(h,w):
    if h == 1 and w == 1:
        return 1
    elif h == 1:
        return w-1
    elif w == 1:
        return h-1
    else:
        return h*w-1

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    dp = [[0 for j in range(W)] for i in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                continue
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            if j - 1 >= 0:
                dp[i][j] += dp[i][j - 1]
    print(dp[H - 1][W - 1])

=======
Suggestion 4

def dfs(i,j):
    if i==H-1 and j==W-1:
        return 1
    if i==H-1:
        if grid[i][j+1]=='#':
            return 1
        else:
            return dfs(i,j+1)+1
    if j==W-1:
        if grid[i+1][j]=='#':
            return 1
        else:
            return dfs(i+1,j)+1
    if grid[i+1][j]=='#':
        return dfs(i,j+1)+1
    if grid[i][j+1]=='#':
        return dfs(i+1,j)+1
    return max(dfs(i+1,j),dfs(i,j+1))+1

H,W=map(int,input().split())
grid=[]
for i in range(H):
    grid.append(list(input()))
print(dfs(0,0))

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    c = [input() for i in range(h)]
    print(walk(h, w, c))

=======
Suggestion 6

def isWall(x, y):
    if x >= 0 and x < H and y >= 0 and y < W:
        if maze[x][y] == '#':
            return True
    return False

=======
Suggestion 7

def solve(H, W, C):
    #dp[i][j]表示从(i, j)开始的最大路径数
    dp = [[0 for j in range(W)] for i in range(H)]
    dp[H - 1][W - 1] = 1
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if C[i][j] == '#':
                continue
            if i + 1 < H:
                dp[i][j] = (dp[i][j] + dp[i + 1][j]) % 1000000007
            if j + 1 < W:
                dp[i][j] = (dp[i][j] + dp[i][j + 1]) % 1000000007
    return dp[0][0]

=======
Suggestion 8

def dfs(x, y):
    global ans
    ans += 1
    maze[x][y] = '#'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx) and (nx < H) and (0 <= ny) and (ny < W) and (maze[nx][ny] == '.'):
            dfs(nx, ny)

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0
dfs(0, 0)
print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    c = [input() for _ in range(H)]
    print(H, W)
    print(c)
    print(c[0][1])
    print(c[1][0])
    print(c[0][0])

    # for i in range(H):
    #     for j in range(W):
    #         print(c[i][j])

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    print(dp[h - 1][w - 1] % (10 ** 9 + 7))

main()
