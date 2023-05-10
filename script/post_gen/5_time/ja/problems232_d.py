Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    H, W = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(input())
    ans = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == "#":
                continue
            if i == 0:
                ans += 1
                continue
            if j == 0:
                ans += 1
                continue
            if C[i-1][j] == "#" and C[i][j-1] == "#":
                continue
            ans += 1
    print(ans)

=======
Suggestion 2

def solve():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1 if C[0][0] == '.' else 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
    print(dp[H - 1][W - 1])

=======
Suggestion 4

def solve():
    # 解答を返す
    return

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if a[i][j] == "#":
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    print(dp[h - 1][w - 1])

=======
Suggestion 6

def check(x,y):
    if x < 0 or y < 0 or x >= H or y >= W:
        return False
    elif c[x][y] == '#':
        return False
    else:
        return True

=======
Suggestion 7

def main():
    # input
    H, W = map(int, input().split())
    C_s = [input() for _ in range(H)]

    # compute
    ans = 0
    for h in range(H):
        for w in range(W):
            for dh, dw in [(1, 0), (0, 1)]:
                if h+dh < H and w+dw < W:
                    if C_s[h][w] == '.' and C_s[h+dh][w+dw] == '.':
                        ans += 1

    # output
    print(ans)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    print(H, W, C)
    print(C[0][0])
    print(C[0][1])
    print(C[1][0])
    print(C[1][1])

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            elif C[i][j] == '#':
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    print(dp[H-1][W-1] % 1000000007)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0]*W for _ in range(H)]
    dp[0][0] = 1 if C[0][0] == '.' else 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    print(dp[H-1][W-1] % (10**9+7))
