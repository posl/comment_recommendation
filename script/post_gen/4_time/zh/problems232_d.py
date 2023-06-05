Synthesizing 10/10 solutions

=======
Suggestion 1

def check(i,j):
    if i < 0 or i >= H or j < 0 or j >= W:
        return False
    if C[i][j] == '#':
        return False
    return True

=======
Suggestion 2

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
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    print(dp[-1][-1])

=======
Suggestion 3

def max_square(maze):
    m = len(maze)
    n = len(maze[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 1
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] if maze[i][0] == '.' else 0
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] if maze[0][j] == '.' else 0
    for i in range(1, m):
        for j in range(1, n):
            if maze[i][j] == '.':
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(input())
    ans = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                ans += 1
    print(ans)

=======
Suggestion 5

def dfs(i,j):
    if i==h-1 and j==w-1:
        return 1
    if i==h-1:
        if a[i][j+1]=='#':
            return 1
        else:
            return dfs(i,j+1)
    if j==w-1:
        if a[i+1][j]=='#':
            return 1
        else:
            return dfs(i+1,j)
    if a[i+1][j]=='#' and a[i][j+1]=='#':
        return 1
    elif a[i+1][j]=='#':
        return dfs(i,j+1)
    elif a[i][j+1]=='#':
        return dfs(i+1,j)
    else:
        return dfs(i,j+1)+dfs(i+1,j)

h,w=map(int,input().split())
a=[list(input()) for _ in range(h)]
print(dfs(0,0))

=======
Suggestion 6

def main():
    H, W = list(map(int, input().strip().split()))
    C = [input().strip() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i][j - 1]) % 1000000007
    print(dp[H - 1][W - 1])

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]

    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[1][1] = 1

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if C[i - 1][j - 1] == '#':
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(dp[H][W] % (10 ** 9 + 7))

=======
Suggestion 8

def f(h, w, s):
    dp = [[0 for i in range(w)] for j in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[h - 1][w - 1]

=======
Suggestion 9

def dfs(x, y):
    global ans
    if x == h - 1 and y == w - 1:
        ans += 1
        return
    if x + 1 < h and s[x + 1][y] == '.':
        dfs(x + 1, y)
    if y + 1 < w and s[x][y + 1] == '.':
        dfs(x, y + 1)
    return

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
dfs(0, 0)
print(ans)

=======
Suggestion 10

def get_input():
    H, W = map(int, input().split())
    C = []
    for h in range(H):
        C.append(list(input()))
    return H, W, C
