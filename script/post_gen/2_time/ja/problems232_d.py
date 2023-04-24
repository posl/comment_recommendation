Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == ".":
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    print(dp[H - 1][W - 1] % (10 ** 9 + 7))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]

    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == "#":
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

    print(dp[H - 1][W - 1] % (10 ** 9 + 7))

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            if i + 1 < H:
                dp[i + 1][j] += dp[i][j]
            if j + 1 < W:
                dp[i][j + 1] += dp[i][j]
    print(dp[-1][-1])

=======
Suggestion 4

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
    print(dp[-1][-1] % (10**9 + 7))

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    print(dp[-1][-1] % (10 ** 9 + 7))
main()

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    print(dp[h - 1][w - 1] % (10 ** 9 + 7))

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    print(dp[H-1][W-1])

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    dp = [[0] * w for i in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                if i != 0:
                    dp[i][j] += dp[i - 1][j]
                if j != 0:
                    dp[i][j] += dp[i][j - 1]
    print(dp[-1][-1] % (10 ** 9 + 7))

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(list(input()))
    dp = [[0 for i in range(W)] for j in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if grid[i][j] == ".":
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    print(dp[H - 1][W - 1] % (10 ** 9 + 7))

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(list(input()))
    
    dp = [[0 for i in range(w)] for j in range(h)]
    dp[0][0] = 1
    
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if c[i][j] == '#':
                continue
            if i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    print(dp[h-1][w-1] % (10**9 + 7))
