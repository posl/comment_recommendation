Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            cnt = 1
            for k in range(1, H+W):
                if i+k < H and j+k < W:
                    if C[i+k][j] == "#" or C[i][j+k] == "#":
                        break
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def solve():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    dp = [[0 for _ in range(W)] for _ in range(H)]
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
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[H-1][W-1]
print(solve())

=======
Suggestion 3

def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    dp = [[0]*w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                continue
            if i != 0:
                dp[i][j] += dp[i-1][j]
            if j != 0:
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= 1000000007
    print(dp[h-1][w-1])

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())

    ans = 0
    x = 0
    y = 0
    while True:
        if x == w - 1 and y == h - 1:
            ans += 1
            break
        if x == w - 1:
            if c[y + 1][x] == ".":
                y += 1
                ans += 1
            else:
                ans += 1
                break
        elif y == h - 1:
            if c[y][x + 1] == ".":
                x += 1
                ans += 1
            else:
                ans += 1
                break
        else:
            if c[y + 1][x] == "." and c[y][x + 1] == ".":
                if c[y + 1][x + 1] == ".":
                    x += 1
                    y += 1
                    ans += 2
                else:
                    ans += 1
                    break
            elif c[y + 1][x] == ".":
                y += 1
                ans += 1
            elif c[y][x + 1] == ".":
                x += 1
                ans += 1
            else:
                ans += 1
                break
    print(ans)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    #print(H, W, C)
    dp = [[0]*W for _ in range(H)]
    dp[0][0] = 1 if C[0][0] == "." else 0
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == "#":
                continue
            if i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #print(dp)
    print(dp[H-1][W-1] % (10**9+7))

=======
Suggestion 6

def get_input():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    return h, w, s

=======
Suggestion 7

def main():
    H,W = map(int,input().split())
    C = [input() for _ in range(H)]
    #print(H,W,C)
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == '#':
                continue
            if i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #print(dp)
    print(dp[H-1][W-1])

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    #print(grid)
    dp = [[0] * (W+1) for i in range(H+1)]
    dp[1][1] = 1
    for i in range(1, H+1):
        for j in range(1, W+1):
            if grid[i-1][j-1] == ".":
                dp[i][j] = max(dp[i][j], dp[i-1][j] + dp[i][j-1])
    print(dp[H][W])

=======
Suggestion 9

def get_input_data():
    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]
    return H, W, C

=======
Suggestion 10

def main():
    H,W = map(int,input().split())
    grid = [[0]*(W+1) for i in range(H+1)]
    for i in range(H):
        grid[i] = list(input())
    dp = [[0]*(W+1) for i in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                continue
            if i+1 < H and grid[i+1][j] == ".":
                dp[i+1][j] += dp[i][j]
            if j+1 < W and grid[i][j+1] == ".":
                dp[i][j+1] += dp[i][j]
    print(dp[H-1][W-1])
