Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == '.':
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '.':
                cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    grid = [input() for i in range(h)]
    dp = [[0 for j in range(w)] for i in range(h)]
    dp[0][0] = 1 if grid[0][0] == '.' else 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= 1000000007
    print(dp[h - 1][w - 1])

=======
Suggestion 4

def solve(h,w,c):
    dp = [[0 for _ in range(w)] for _ in range(h)]
    if c[0][0] == '#':
        dp[0][0] = 0
    else:
        dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if c[i][j] == '#':
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[h-1][w-1]

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(input())
    visited = [[False for _ in range(w)] for _ in range(h)]
    def dfs(i, j):
        if i < 0 or i >= h or j < 0 or j >= w or grid[i][j] == '#' or visited[i][j]:
            return 0
        visited[i][j] = True
        return 1 + dfs(i, j + 1) + dfs(i + 1, j)
    print(dfs(0, 0))

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    c = [input() for i in range(h)]
    print(c)
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == '.':
                ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    h,w = map(int,input().split())
    c = [input() for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    q = [(0,0)]
    visited[0][0] = True
    while q:
        x,y = q.pop(0)
        for dx,dy in [(0,1),(1,0)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<h and 0<=ny<w and c[nx][ny] == '.' and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
    return sum([sum(row) for row in visited])

print(solve())

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    # print(C)
    # print(C[0][0])
    # print(C[0][1])
    # print(C[1][0])
    # print(C[1][1])
    # print(C[2][0])
    # print(C[2][1])
    # print(C[3][0])
    # print(C[3][1])
    # print(C[4][0])
    # print(C[4][1])
    # print(C[0][1])
    # print(C[1][0])
    # print(C[1][1])
    # print(C[2][0])
    # print(C[2][1])
    # print(C[3][0])
    # print(C[3][1])
    # print(C[4][0])
    # print(C[4][1])
    # print(C[0][1])
    # print(C[1][0])
    # print(C[1][1])
    # print(C[2][0])
    # print(C[2][1])
    # print(C[3][0])
    # print(C[3][1])
    # print(C[4][0])
    # print(C[4][1])
    # print(C[0][1])
    # print(C[1][0])
    # print(C[1][1])
    # print(C[2][0])
    # print(C[2][1])
    # print(C[3][0])
    # print(C[3][1])
    # print(C[4][0])
    # print(C[4][1])
    # print(C[0][1])
    # print(C[1][0])
    # print(C[1][1])
    # print(C[2][0])
    # print(C[2][1])
    # print(C[3][0])
    # print(C[3][1])
    # print(C[4][0])
    # print(C[4][1])
    # print(C[0][1])
    # print(C[1][0])
    # print(C[1][1])
    # print(C[2][0])
    # print(C[2][1])
    # print(C[3

=======
Suggestion 9

def main():
    # input
    H, W = map(int, input().split())
    # print(H, W)
    grid = []
    for i in range(H):
        grid.append(list(input()))
    # print(grid)
    # output
    print(visit(H, W, grid))

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    print(grid)
    print(H, W)
