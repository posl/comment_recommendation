Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]

    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]

    print(dp[H - 1][W - 1] % (10**9 + 7))

main()

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if i > 0 and grid[i - 1][j] == '.':
                dp[i][j] += dp[i - 1][j]
            if j > 0 and grid[i][j - 1] == '.':
                dp[i][j] += dp[i][j - 1]
    print(dp[h - 1][w - 1])

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    grid = [list(input()) for i in range(h)]
    dp = [[0] * w for i in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if grid[i][j] == '.':
                if i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[h - 1][w - 1] % (10 ** 9 + 7))

=======
Suggestion 4

def main():
    h,w = map(int,input().split())
    c = [list(input()) for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if c[i][j] == '#':
                dp[i][j] = 0
            else:
                if i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[h-1][w-1])

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(list(input()))

    dp = [[0 for i in range(W)] for j in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= 1000000007
    print(dp[H - 1][W - 1])

=======
Suggestion 6

def main():
    # H, W = map(int, input().split())
    # C = [input() for _ in range(H)]
    H, W = 5, 5
    C = [
        ".....",
        ".....",
        ".....",
        ".....",
        ".....",
    ]
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1]
                continue
            if j == 0:
                dp[i][j] = dp[i - 1][j]
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[-1][-1])

main()

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    #C = [list(map(str, input().split())) for _ in range(H)]
    C = [list(map(str, input())) for _ in range(H)]
    #print(C)
    #print(C[0][0])
    #print(C[0][1])
    #print(C[0][2])
    #print(C[0][3])
    #print(C[0][4])
    #print(C[1][0])
    #print(C[1][1])
    #print(C[1][2])
    #print(C[1][3])
    #print(C[1][4])
    #print(C[2][0])
    #print(C[2][1])
    #print(C[2][2])
    #print(C[2][3])
    #print(C[2][4])
    #print(C[3][0])
    #print(C[3][1])
    #print(C[3][2])
    #print(C[3][3])
    #print(C[3][4])
    #print(C[4][0])
    #print(C[4][1])
    #print(C[4][2])
    #print(C[4][3])
    #print(C[4][4])

    #print(C[0][0] == ".")
    #print(C[0][0] == "#")
    #print(C[1][0] == ".")
    #print(C[1][0] == "#")
    #print(C[2][0] == ".")
    #print(C[2][0] == "#")
    #print(C[3][0] == ".")
    #print(C[3][0] == "#")
    #print(C[4][0] == ".")
    #print(C[4][0] == "#")
    #print(C[0][1] == ".")
    #print(C[0][1] == "#")
    #print(C[1][1] == ".")
    #print(C[1][1] == "#")
    #print(C[2][1] == ".")
    #print(C[2][1] == "#")
    #print(C[3][1] == ".")
    #print(C[3][1] == "#")
    #print(C[

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]

    # dp[i][j] := (1,1) から (i,j) までの最短距離
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1])
            dp[i][j] += 1

    print(dp[-1][-1])

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]

    # dp[i][j] = (i, j) にたどり着くのに必要な最小コスト
    dp = [[0] * W for _ in range(H)]

    # 初期条件
    dp[0][0] = 1

    # 動的計画法
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == "#":
                dp[i][j] = 0
            else:
                if i >= 1:
                    dp[i][j] += dp[i - 1][j]
                if j >= 1:
                    dp[i][j] += dp[i][j - 1]

    print(dp[H - 1][W - 1] % (10 ** 9 + 7))

=======
Suggestion 10

def read():
    return int(input())
