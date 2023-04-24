Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if C[h][w] == "#":
                continue
            if h > 0:
                dp[h][w] += dp[h - 1][w]
            if w > 0:
                dp[h][w] += dp[h][w - 1]
    print(dp[H - 1][W - 1] % (10 ** 9 + 7))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    print(dp[-1][-1] % (10 ** 9 + 7))

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    print(dp[-1][-1] % (10 ** 9 + 7))

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if grid[i][j] == '#':
                continue
            if i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[-1][-1] % (10**9 + 7))

=======
Suggestion 5

def solve():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if C[h][w] == "#":
                continue
            if h > 0:
                dp[h][w] += dp[h - 1][w]
            if w > 0:
                dp[h][w] += dp[h][w - 1]
    print(dp[-1][-1] % (10 ** 9 + 7))

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    print(dp[-1][-1] % (10 ** 9 + 7))

=======
Suggestion 7

def solve():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == '.':
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    print(dp[H - 1][W - 1])
    return

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[0][0] = True
    queue = [[0, 0]]
    count = 0
    while queue:
        x, y = queue.pop(0)
        count += 1
        for dx, dy in [[1, 0], [0, 1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])
    print(count)

=======
Suggestion 9

def check(x, y):
    if x >= 0 and x < w and y >= 0 and y < h and grid[y][x] == '.':
        return True
    return False

h, w = map(int, input().split())
grid = [input() for _ in range(h)]
ans = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == '.':
            ans += 1
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                grid[y][x] = '#'
                for dx, dy in [(1, 0), (0, 1)]:
                    if check(x + dx, y + dy):
                        stack.append((x + dx, y + dy))
print(ans)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())

    # dp[i][j] = (i,j)にたどり着く方法の数
    dp = [[0] * W for i in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            if i != 0:
                dp[i][j] += dp[i-1][j]
            if j != 0:
                dp[i][j] += dp[i][j-1]

    print(dp[H-1][W-1])
