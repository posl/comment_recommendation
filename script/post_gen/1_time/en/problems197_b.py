Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    s = [input() for _ in range(h)]
    ans = 1
    for i in range(x+1, h):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(x-1, -1, -1):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(y+1, w):
        if s[x][i] == '#':
            break
        ans += 1
    for i in range(y-1, -1, -1):
        if s[x][i] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    s = [input() for _ in range(h)]
    ans = 1
    for i in range(x-1, -1, -1):
        if s[i][y] == '.':
            ans += 1
        else:
            break
    for i in range(x+1, h):
        if s[i][y] == '.':
            ans += 1
        else:
            break
    for j in range(y-1, -1, -1):
        if s[x][j] == '.':
            ans += 1
        else:
            break
    for j in range(y+1, w):
        if s[x][j] == '.':
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 3

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1

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
Suggestion 4

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]

    X -= 1
    Y -= 1

    ans = 1
    for i in range(X - 1, -1, -1):
        if S[i][Y] == "#":
            break
        ans += 1
    for i in range(X + 1, H):
        if S[i][Y] == "#":
            break
        ans += 1
    for i in range(Y - 1, -1, -1):
        if S[X][i] == "#":
            break
        ans += 1
    for i in range(Y + 1, W):
        if S[X][i] == "#":
            break
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    cnt = 1
    for i in range(X-2, -1, -1):
        if S[i][Y-1] == '#':
            break
        cnt += 1
    for i in range(X, H):
        if S[i][Y-1] == '#':
            break
        cnt += 1
    for j in range(Y-2, -1, -1):
        if S[X-1][j] == '#':
            break
        cnt += 1
    for j in range(Y, W):
        if S[X-1][j] == '#':
            break
        cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 1
    for i in range(x - 1, -1, -1):
        if s[i][y - 1] == '#':
            break
        ans += 1
    for i in range(x, h):
        if s[i][y - 1] == '#':
            break
        ans += 1
    for i in range(y - 1, -1, -1):
        if s[x - 1][i] == '#':
            break
        ans += 1
    for i in range(y, w):
        if s[x - 1][i] == '#':
            break
        ans += 1
    print(ans - 3)

=======
Suggestion 7

def main():
    H, W, X, Y = [int(i) for i in input().split()]
    S = [input() for _ in range(H)]
    ans = 1
    for i in range(X - 1, 0, -1):
        if S[i - 1][Y - 1] == '#':
            break
        ans += 1
    for i in range(X + 1, H + 1):
        if S[i - 1][Y - 1] == '#':
            break
        ans += 1
    for j in range(Y - 1, 0, -1):
        if S[X - 1][j - 1] == '#':
            break
        ans += 1
    for j in range(Y + 1, W + 1):
        if S[X - 1][j - 1] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 8

def main():
    # Read input
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]

    # Count visible squares
    ans = 1
    for i in range(X - 1, 0, -1):
        if S[i - 1][Y - 1] == ".":
            ans += 1
        else:
            break
    for i in range(X + 1, H + 1):
        if S[i - 1][Y - 1] == ".":
            ans += 1
        else:
            break
    for j in range(Y - 1, 0, -1):
        if S[X - 1][j - 1] == ".":
            ans += 1
        else:
            break
    for j in range(Y + 1, W + 1):
        if S[X - 1][j - 1] == ".":
            ans += 1
        else:
            break

    # Output
    print(ans)

=======
Suggestion 9

def main():
    # Get input
    h, w, x, y = map(int, input().split())
    s = [input() for i in range(h)]
    # Count visible squares
    count = 1
    for i in range(x - 2, -1, -1):
        if s[i][y - 1] == "#":
            break
        count += 1
    for i in range(x, h):
        if s[i][y - 1] == "#":
            break
        count += 1
    for i in range(y - 2, -1, -1):
        if s[x - 1][i] == "#":
            break
        count += 1
    for i in range(y, w):
        if s[x - 1][i] == "#":
            break
        count += 1
    # Print answer
    print(count)

=======
Suggestion 10

def main():
    """main function"""
    # Input
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    # Solve
    ans = 1
    for i in range(x - 1, -1, -1):
        if s[i][y - 1] == '#':
            break
        ans += 1
    for i in range(x, h):
        if s[i][y - 1] == '#':
            break
        ans += 1
    for i in range(y - 1, -1, -1):
        if s[x - 1][i] == '#':
            break
        ans += 1
    for i in range(y, w):
        if s[x - 1][i] == '#':
            break
        ans += 1
    # Output
    print(ans - 3)
