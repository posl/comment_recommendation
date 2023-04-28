Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    x -= 1
    y -= 1
    ans = 1
    for i in range(x-1,-1,-1):
        if s[i][y] == "#":
            break
        ans += 1
    for i in range(x+1,h):
        if s[i][y] == "#":
            break
        ans += 1
    for i in range(y-1,-1,-1):
        if s[x][i] == "#":
            break
        ans += 1
    for i in range(y+1,w):
        if s[x][i] == "#":
            break
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    X -= 1
    Y -= 1
    ans = 1
    for i in range(Y+1, W):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y-1, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    h, w, x, y = map(int, input().split())
    x = x - 1
    y = y - 1
    s = []
    for i in range(h):
        s.append(input())
    count = 0
    for i in range(x, h):
        if s[i][y] == '#':
            break
        else:
            count += 1
    for i in range(x-1, -1, -1):
        if s[i][y] == '#':
            break
        else:
            count += 1
    for i in range(y, w):
        if s[x][i] == '#':
            break
        else:
            count += 1
    for i in range(y-1, -1, -1):
        if s[x][i] == '#':
            break
        else:
            count += 1
    print(count-3)

=======
Suggestion 4

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1
    ans = 0
    for i in range(X, -1, -1):
        if S[i][Y] == "#":
            break
        ans += 1
    for i in range(X+1, H):
        if S[i][Y] == "#":
            break
        ans += 1
    for j in range(Y, -1, -1):
        if S[X][j] == "#":
            break
        ans += 1
    for j in range(Y+1, W):
        if S[X][j] == "#":
            break
        ans += 1
    print(ans-3)

=======
Suggestion 5

def main():
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    x -= 1
    y -= 1

    ans = 1
    for i in range(x+1, h):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(x-1, -1, -1):
        if s[i][y] == '#':
            break
        ans += 1
    for j in range(y+1, w):
        if s[x][j] == '#':
            break
        ans += 1
    for j in range(y-1, -1, -1):
        if s[x][j] == '#':
            break
        ans += 1

    print(ans)

=======
Suggestion 6

def main():
    h, w, x, y = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    x -= 1
    y -= 1

    ans = 1
    for i in range(x+1, h):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(x-1, -1, -1):
        if s[i][y] == '#':
            break
        ans += 1
    for j in range(y+1, w):
        if s[x][j] == '#':
            break
        ans += 1
    for j in range(y-1, -1, -1):
        if s[x][j] == '#':
            break
        ans += 1

    print(ans)

=======
Suggestion 7

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]

    X -= 1
    Y -= 1

    count = 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        count += 1

    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        count += 1

    for i in range(Y+1, W):
        if S[X][i] == '#':
            break
        count += 1

    for i in range(Y-1, -1, -1):
        if S[X][i] == '#':
            break
        count += 1

    print(count)

=======
Suggestion 8

def main():
    h, w, x, y = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())

    count = 0
    for i in range(x-1, -1, -1):
        if s[i][y-1] == '.':
            count += 1
        else:
            break

    for i in range(x, h):
        if s[i][y-1] == '.':
            count += 1
        else:
            break

    for i in range(y-2, -1, -1):
        if s[x-1][i] == '.':
            count += 1
        else:
            break

    for i in range(y, w):
        if s[x-1][i] == '.':
            count += 1
        else:
            break

    print(count)

=======
Suggestion 9

def main():
    h,w,x,y = map(int, input().split())
    s = [input() for _ in range(h)]
    x-=1
    y-=1
    cnt = 1
    for i in range(x+1,h):
        if s[i][y] == '#':
            break
        cnt += 1
    for i in range(x-1,-1,-1):
        if s[i][y] == '#':
            break
        cnt += 1
    for i in range(y+1,w):
        if s[x][i] == '#':
            break
        cnt += 1
    for i in range(y-1,-1,-1):
        if s[x][i] == '#':
            break
        cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    # Standard Input
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    # Initialize
    count = 1
    # Count up
    # Horizontal
    for i in range(X, H):
        if S[i-1][Y-1] == '#':
            break
        else:
            count += 1
    for i in range(X-2, -1, -1):
        if S[i][Y-1] == '#':
            break
        else:
            count += 1
    # Vertical
    for i in range(Y, W):
        if S[X-1][i-1] == '#':
            break
        else:
            count += 1
    for i in range(Y-2, -1, -1):
        if S[X-1][i] == '#':
            break
        else:
            count += 1
    # Standard Output
    print(count)
