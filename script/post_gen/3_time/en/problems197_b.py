Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    S = [input() for _ in range(H)]
    ans = 1
    for i in range(X - 1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X + 1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for j in range(Y - 1, -1, -1):
        if S[X][j] == '#':
            break
        ans += 1
    for j in range(Y + 1, W):
        if S[X][j] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    x -= 1
    y -= 1
    ans = 1
    for i in range(x-1, -1, -1):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(x+1, h):
        if s[i][y] == '#':
            break
        ans += 1
    for j in range(y-1, -1, -1):
        if s[x][j] == '#':
            break
        ans += 1
    for j in range(y+1, w):
        if s[x][j] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    s = [input() for _ in range(h)]
    ans = 1
    for i in range(x - 1, -1, -1):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(x + 1, h):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(y - 1, -1, -1):
        if s[x][i] == '#':
            break
        ans += 1
    for i in range(y + 1, w):
        if s[x][i] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(X, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(Y, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y, W):
        if S[X][i] == '#':
            break
        ans += 1
    print(ans - 3)

=======
Suggestion 5

def main():
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    s = [input() for i in range(h)]
    ans = 1
    for i in range(x+1, h):
        if s[i][y] == ".":
            ans += 1
        else:
            break
    for i in range(x-1, -1, -1):
        if s[i][y] == ".":
            ans += 1
        else:
            break
    for i in range(y+1, w):
        if s[x][i] == ".":
            ans += 1
        else:
            break
    for i in range(y-1, -1, -1):
        if s[x][i] == ".":
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 6

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1
    count = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        count += 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        count += 1
    for j in range(Y-1, -1, -1):
        if S[X][j] == '#':
            break
        count += 1
    for j in range(Y+1, W):
        if S[X][j] == '#':
            break
        count += 1
    print(count)

=======
Suggestion 7

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1
    count = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == "#":
            break
        count += 1
    for i in range(X+1, H):
        if S[i][Y] == "#":
            break
        count += 1
    for j in range(Y-1, -1, -1):
        if S[X][j] == "#":
            break
        count += 1
    for j in range(Y+1, W):
        if S[X][j] == "#":
            break
        count += 1
    print(count)

main()

=======
Suggestion 8

def main():
    H, W, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    S = [input() for i in range(H)]
    ans = 0
    for i in range(X, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(Y, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y, W):
        if S[X][i] == '#':
            break
        ans += 1
    print(ans - 3)

=======
Suggestion 9

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 1
    for i in range(1, H):
        if S[X - 1 - i][Y - 1] == "#":
            break
        ans += 1
    for i in range(1, H):
        if S[X - 1 + i][Y - 1] == "#":
            break
        ans += 1
    for i in range(1, W):
        if S[X - 1][Y - 1 - i] == "#":
            break
        ans += 1
    for i in range(1, W):
        if S[X - 1][Y - 1 + i] == "#":
            break
        ans += 1
    print(ans)
