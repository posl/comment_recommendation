Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1
    ans = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(Y-1, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y+1, W):
        if S[X][i] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    S = []
    for i in range(H):
        S.append(input())
    ans = 1
    for i in range(X - 1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X + 1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(Y - 1, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y + 1, W):
        if S[X][i] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X, Y = X - 1, Y - 1
    ans = 1
    for i in range(X + 1, H):
        if S[i][Y] == "#":
            break
        ans += 1
    for i in range(X - 1, -1, -1):
        if S[i][Y] == "#":
            break
        ans += 1
    for i in range(Y + 1, W):
        if S[X][i] == "#":
            break
        ans += 1
    for i in range(Y - 1, -1, -1):
        if S[X][i] == "#":
            break
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    S = []
    for _ in range(H):
        S.append(input())
    ans = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(Y-1, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y+1, W):
        if S[X][i] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1

    ans = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for j in range(Y-1, -1, -1):
        if S[X][j] == '#':
            break
        ans += 1
    for j in range(Y+1, W):
        if S[X][j] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1

    ans = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == "#":
            break
        ans += 1
    for i in range(X+1, H):
        if S[i][Y] == "#":
            break
        ans += 1
    for i in range(Y-1, -1, -1):
        if S[X][i] == "#":
            break
        ans += 1
    for i in range(Y+1, W):
        if S[X][i] == "#":
            break
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    X -= 1
    Y -= 1
    cnt = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        cnt += 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        cnt += 1
    for i in range(Y-1, -1, -1):
        if S[X][i] == '#':
            break
        cnt += 1
    for i in range(Y+1, W):
        if S[X][i] == '#':
            break
        cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    H, W, X, Y = map(int, input().split())
    S = [list(input()) for i in range(H)]

    count = 1
    for i in range(X - 2, -1, -1):
        if S[i][Y - 1] == '#':
            break
        count += 1
    for i in range(X, H):
        if S[i][Y - 1] == '#':
            break
        count += 1
    for i in range(Y - 2, -1, -1):
        if S[X - 1][i] == '#':
            break
        count += 1
    for i in range(Y, W):
        if S[X - 1][i] == '#':
            break
        count += 1
    print(count)

=======
Suggestion 9

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    count = 0
    # 上下左右の方向を表すベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        x = X - 1
        y = Y - 1
        while True:
            x += dx[i]
            y += dy[i]
            if 0 <= x < H and 0 <= y < W and S[x][y] == '.':
                count += 1
            else:
                break
    print(count + 1)

=======
Suggestion 10

def main():
    # Take the input
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]

    # Start from (X, Y) and go in all 4 directions
    # until you hit a wall or an obstacle
    count = 1
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x, y = X-1, Y-1
        while True:
            x += dx
            y += dy
            if x < 0 or x >= H or y < 0 or y >= W or S[x][y] == '#':
                break
            count += 1

    # Print the answer
    print(count)
